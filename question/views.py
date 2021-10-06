from django.shortcuts import render, redirect
from .models import Question, Choice

import random

# Create your views here.


def caculate(arr, id):

    p1, p2 = 0, 0
    result = []

    for a in arr:
        if a.question_id == id:
            result.append(a)

            if a.pick == 1:
                p1 += 1
            else:
                p2 += 1

    if p1 + p2 != 0:
        p1_per = round(p1 * 100 / (p1 + p2), 2)
        p2_per = round(p2 * 100 / (p1 + p2), 2)

    else:
        p1_per, p2_per = 0, 0

    return (p1, p2, p1_per, p2_per, result)


def index(request):

    question = Question.objects.all()

    context = {
        'question': question,
    }

    return render(request, 'index.html', context)


def lucky(request):

    total = Question.objects.all()

    q_id = random.randrange(0, len(total))
    question = total[q_id]

    choices = Choice.objects.all()

    p1, p2, p1_per, p2_per, result = caculate(choices, question.id)

    context = {
        'question': question,
        'p1': p1,
        'p2': p2,
        'p1_per': p1_per,
        'p2_per': p2_per,
        'result': result,
    }

    return render(request, 'lucky.html', context)


def create(request):

    if request.method == 'POST':

        question = request.POST.get('question')
        answer1 = request.POST.get('answer1')
        answer2 = request.POST.get('answer2')

        Question.objects.create(
            question=question, answer1=answer1, answer2=answer2)

        return redirect('question:index')
    else:
        return render(request, 'create.html')


def update(request, id):

    question = Question.objects.get(id=id)

    if request.method == 'POST':

        question.question = request.POST.get('question')
        question.answer1 = request.POST.get('answer1')
        question.answer2 = request.POST.get('answer2')

        question.save()

        return redirect('question:index')
    else:

        context = {
            'question': question,
        }

        return render(request, 'update.html', context)


def delete(request, id):

    question = Question.objects.get(id=id)
    question.delete()

    return redirect('question:index')


def choice(request, id, select):

    question = Question.objects.get(id=id)
    Choice.objects.create(pick=select, comment='None', question=question)

    return redirect('question:detail', id)


def detail(request, id):

    question = Question.objects.get(id=id)
    choices = Choice.objects.all()

    p1, p2, p1_per, p2_per, result = caculate(choices, id)

    context = {
        'question': question,
        'p1': p1,
        'p2': p2,
        'p1_per': p1_per,
        'p2_per': p2_per,
        'result': result,
        'choices': choices,
    }

    return render(request, 'detail.html', context)


def choice_delete(request, q_id, c_id):

    Choice.objects.get(id=c_id).delete()

    return redirect('question:detail', q_id)

import random

from django.shortcuts import render, redirect

from .models import Question, Choice


def caculate(choices, question_id):
    choice1 = len(choices.filter(pick=1))
    choice2 = len(choices.filter(pick=2))

    if not (choice1 + choice2):
        percent1 = percent2 = 0
    else:
        percent1 = round(choice1 * 100 / (choice1 + choice2), 2)
        percent2 = round(choice2 * 100 / (choice1 + choice2), 2)

    return choice1, choice2, percent1, percent2


def index(request):
    context = {
        'questions': Question.objects.all(),
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        Question.objects.create(
            question=request.POST.get('question'),
            answer1=request.POST.get('answer1'),
            answer2=request.POST.get('answer2'),
        )
        return redirect('question:index')
    else:
        return render(request, 'create.html')


def update(request, question_id):
    question = Question.objects.get(id=question_id)
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


def delete(request, question_id):
    Question.objects.get(id=question_id).delete()
    return redirect('question:index')


def create_choice(request, question_id, select):
    Choice.objects.create(
        pick=select,
        comment=random.choice(['a', 'b', 'c', 'd', 'e']),
        question=Question.objects.get(id=question_id)
    )
    return redirect('question:detail', question_id)


def delete_choice(request, question_id, choice_id):
    Choice.objects.get(id=choice_id).delete()
    return redirect('question:detail', question_id)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)

    choice1, choice2, percent1, percent2 = caculate(choices, question_id)

    context = {
        'question': question, 'choices': choices,
        'choice1': choice1, 'choice2': choice2,
        'percent1': percent1, 'percent2': percent2,
    }

    return render(request, 'detail.html', context)

from django.db import models

# Create your models here.

class Question(models.Model):

    question = models.CharField(max_length=100)
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.CharField(max_length=100)
    
from django.db import models
from django.contrib.auth.models import User
from module.models import Licence, Module

class Exam(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    type_license = models.ForeignKey(Licence, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('MC', 'Multiple Choice'),
        ('TF', 'True/False')
    ]

    question = models.CharField(max_length=200)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, to_field='name')
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE_CHOICES)
    answerA = models.CharField(max_length=100)
    answerB = models.CharField(max_length=100)
    answerC = models.CharField(max_length=100, blank=True, null=True)
    answerD = models.CharField(max_length=100, blank=True, null=True)
    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Answer A'),
            ('B', 'Answer B'),
            ('C', 'Answer C'),
            ('D', 'Answer D'),
        ],
        null=True
    )    

    def __str__(self):
        return self.question

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    id_exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return self.id_user.username
# Create your models here.

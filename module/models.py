from django.db import models
from django.utils import timezone

class Licence(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=40, unique=True)
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE, to_field='name')
    created_at = models.DateTimeField(default=timezone.now) 

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

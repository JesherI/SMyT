from django.db import models
from django.utils import timezone

class Licence(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=40)
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE, to_field='name')
    created_at = models.DateTimeField(default=timezone.now) 
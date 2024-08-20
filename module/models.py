from django.db import models
from django.utils import timezone

class Licence(models.Model):
    name = models.CharField(max_length=40, unique=True)
    letter = models.CharField(max_length=2, null=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=40, unique=True)
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE, to_field='name')
    description = models.TextField(max_length=500, default='')  # Valor predeterminado agregado aquí
    created_at = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.name



from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class User(models.Model):
    username = models.CharField(max_length=40, null=True)
    name = models.CharField(max_length=40, null=True)
    first_lastname = models.CharField(max_length=40, null=True)
    second_lastname = models.CharField(max_length=40, null=True)
    admin = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100, null=True)
    curp = models.CharField(max_length=18, unique=True)
    password = models.CharField(max_length=100, null=True)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

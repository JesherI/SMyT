from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Student(User):
    second_lastname = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100, null=True)
    curp = models.CharField(max_length=18, unique=False)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

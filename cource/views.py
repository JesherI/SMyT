from django.shortcuts import render
from rest_framework import viewsets
from .models import CourseIntro
from .serializers import CourseIntroSerializer

class CourseIntroViewSet(viewsets.ModelViewSet):
    queryset = CourseIntro.objects.all()
    serializer_class = CourseIntroSerializer
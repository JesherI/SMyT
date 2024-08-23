from rest_framework import serializers
from .models import CourseIntro

class CourseIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseIntro
        fields = '__all__'
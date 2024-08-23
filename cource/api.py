from rest_framework import viewsets, permissions
from .models import CourseIntro
from .serializers import CourseIntroSerializer

class CourseIntroViewSet(viewsets.ModelViewSet):
    queryset = CourseIntro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseIntroSerializer
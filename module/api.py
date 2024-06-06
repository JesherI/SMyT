from rest_framework import viewsets, permissions
from .models import Module, Licence, Question
from .serializers import ModuleSerializer, LicenceSerializer, QuestionSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ModuleSerializer

class LicenceViewSet(viewsets.ModelViewSet):
    queryset = Licence.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LicenceSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionSerializer

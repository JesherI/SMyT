from rest_framework import viewsets, permissions
from .models import Module, Licence
from .serializers import ModuleSerializer, LicenceSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ModuleSerializer

class LicenceViewSet(viewsets.ModelViewSet):
    queryset = Licence.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LicenceSerializer


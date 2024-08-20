from rest_framework import serializers
from .models import Module, Licence 

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'name', 'licence', 'created_at')
        read_only_fields = ['id', 'created_at']

class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licence
        fields = ('id', 'name', 'letter', 'description')
        read_only_fields = ['id']


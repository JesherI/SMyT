from rest_framework import serializers
from .models import Comments

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'user','module', 'comments', 'created_at')
        read_only_fields = ['id', 'created_at']

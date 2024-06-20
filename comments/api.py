from rest_framework import viewsets, permissions
from .models import Comments
from .serializers import CommentsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentsSerializer

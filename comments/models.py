from django.db import models
from user.models import Student

class Comments(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    comments = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment by {self.user}'

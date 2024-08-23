from django.db import models

class CourseIntro(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    video_link = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    extra_file = models.FileField(upload_to='files/', null=True, blank=True)

    def _str_(self):
        return self.title
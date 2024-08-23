from rest_framework import routers
from .api import CourseIntroViewSet

router = routers.DefaultRouter()
router.register(r'course', CourseIntroViewSet, 'cursos')

urlpatterns = router.urls
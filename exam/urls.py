from rest_framework import routers
from .api import ExamViewSet, QuestionViewSet, ResultViewSet

router = routers.DefaultRouter()

router.register(r'Exam', ExamViewSet, 'Exam')
router.register(r'question', QuestionViewSet, 'Question')
router.register(r'Result', ResultViewSet, 'Result')

urlpatterns = router.urls

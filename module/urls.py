from rest_framework import routers
from .api import ModuleViewSet, LicenceViewSet, QuestionViewSet

router = routers.DefaultRouter()

router.register(r'module', ModuleViewSet, 'Module')
router.register(r'licences', LicenceViewSet, 'Licence')
router.register(r'questions', QuestionViewSet, 'Question')


urlpatterns = router.urls

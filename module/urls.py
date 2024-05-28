from rest_framework import routers
from .api import ModuleViewSet, LicenceViewSet

router = routers.DefaultRouter()

router.register(r'module', ModuleViewSet, 'Module')
router.register(r'licences', LicenceViewSet, 'Licence')

urlpatterns = router.urls

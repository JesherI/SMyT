from rest_framework import routers
from .api import CommentsViewSet

router = routers.DefaultRouter()

router.register(r'commentarios', CommentsViewSet, 'comments')


urlpatterns = router.urls

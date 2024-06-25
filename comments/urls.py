from rest_framework import routers
from .api import CommentsViewSet

router = routers.DefaultRouter()

router.register(r'comments', CommentsViewSet, 'comments')


urlpatterns = router.urls

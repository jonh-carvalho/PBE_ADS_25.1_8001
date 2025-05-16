from rest_framework.routers import DefaultRouter
from .views import ContentViewSet
from .views import PlaylistViewSet

router = DefaultRouter()
router.register(r'contents', ContentViewSet)
router.register(r'playlists', PlaylistViewSet, basename='playlist')

urlpatterns = router.urls
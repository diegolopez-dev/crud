from rest_framework import routers
from .api import ProjectViewsets

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewsets, 'projects')
urlpatterns = router.urls



from rest_framework import routers
from .views import LivrariaViewSet

router = routers.DefaultRouter()
router.register(r'', LivrariaViewSet)
urlpatterns = router.urls
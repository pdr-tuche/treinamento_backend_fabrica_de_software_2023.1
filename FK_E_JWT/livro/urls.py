from rest_framework import routers
from .views import LivroViewset

router = routers.DefaultRouter()
router.register(r'', LivroViewset)
urlpatterns = router.urls
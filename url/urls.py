from .views import Urlviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'url',Urlviewset,basename='url')

urlpatterns = router.urls
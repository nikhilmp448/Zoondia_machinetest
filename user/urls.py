from .views import UserRegisterViewset,AdminViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'register',UserRegisterViewset,basename='register')
router.register(r'adminbase',AdminViewset,basename='admin')


urlpatterns = router.urls
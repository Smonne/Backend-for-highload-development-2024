from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SecureModelViewSet

router = DefaultRouter()
router.register(r'secure-model', SecureModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

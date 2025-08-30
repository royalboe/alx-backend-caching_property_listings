from .views import PropertyViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = router.urls
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcessStepViewSet

router = DefaultRouter()
router.register(r'process-steps', ProcessStepViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

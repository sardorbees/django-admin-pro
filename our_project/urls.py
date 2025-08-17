from django.urls import path
from .views import CardListAPIView

urlpatterns = [
    path('cards/', CardListAPIView.as_view(), name='cards-list'),
]

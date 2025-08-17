from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib import admin
from .views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", RegisterView.as_view()),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("profile/", ProfileView.as_view()),
]

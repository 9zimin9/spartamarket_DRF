from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, ProfileView


urlpatterns = [
    # 회원가입 api 엔드포인트
    path("", RegisterView.as_view(), name="register"),
    # 로그인 api 엔드포인트
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("<str:username>/", ProfileView.as_view(), name="profile"),
]

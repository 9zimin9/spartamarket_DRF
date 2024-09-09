from django.urls import path
from .views import RegisterView
from .views import LoginView


urlpatterns = [
    # 회원가입 api 엔드포인트
    path("", RegisterView.as_view(), name="register"),
    # 로그인 api 엔드포인트
    path("login/", LoginView.as_view(), name="login"),
]

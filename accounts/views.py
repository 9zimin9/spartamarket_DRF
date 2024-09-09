from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.authtoken.models import (
# )  # Token에서 RefreshToken으로 변경/JWT 토큰

from django.contrib.auth import authenticate
from .serializers import UserSerializer


# 회원가입 기능 구현
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # 유효성 검사를 통과했다면
        if serializer.is_valid():
            serializer.save()  # 사용자 저장
            return Response(
                {"message": "회원가입 완료!"},
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        # 유효성 검사를 통과 못햇다면, 400 에러
        return Response(
            {"message": "회원가입 실패ㅠ"},
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# 로그인 api (토큰하는거 어렵,,, 이 부분 gpt에게 물어봄,,^^/JWT 토큰)
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            # JWT 토큰 생성( 더 어려운 것 같음 / 수업 내용으로 주말에 다시 해볼 부분)
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "로그인 실패"}, status=status.HTTP_400_BAD_REQUEST
            )

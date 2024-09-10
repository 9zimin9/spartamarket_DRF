from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# from rest_framework.authtoken.models import (
# )  # Token에서 RefreshToken으로 변경/JWT 토큰
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .models import CustomUser


# 회원가입 기능 구현
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # 유효성 검사를 통과했다면
        if serializer.is_valid():
            serializer.save()  # 사용자 저장
            return Response(
                {"message": "회원가입 완료!"},
                status=status.HTTP_201_CREATED,
            )
        # 유효성 검사를 통과 못햇다면, 400 에러
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# 프로필 조회(로그인 시에만 조회 가능)- 원래loginview로 했다가 프로필 조회 기능과 합침침
CustomUser = get_user_model()


class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        username = self.kwargs["username"]
        user = generics.get_object_or_404(CustomUser, username=username)
        return user

    # 로그인한 사람만 본인 프로필 조회 가능
    def get(self, request, *args, **kwargs):
        if request.user.username != self.kwargs["username"]:
            return Response(
                {"detail": "You are not allowed to view this profile."}, status=403
            )
        return super().get(request, *args, **kwargs)

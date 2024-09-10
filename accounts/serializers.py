from rest_framework import serializers
from .models import CustomUser  #  User를 CustomUser로 변경

# 회원가입할 때,


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "email",
            "name",
            "nickname",
            "birthday",
            "gender",
            "intro",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }  # write_only: 비밀번호는 읽지 않고 저장만

    # 이메일 유효성 검사
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("이 이메일은 이미 사용 중입니다.")
        return value

    # 비밀번호 해시화를 위해 create 메소드 오버라이딩--암호화 (어려워서 질문하러감)
    def create(self, validated_data):
        # 비밀번호를 자동으로 해시화하여 저장
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            name=validated_data["name"],
            nickname=validated_data["nickname"],
            birthday=validated_data["birthday"],
            gender=validated_data.get("gender", ""),
            intro=validated_data.get("intro", ""),
        )
        return user

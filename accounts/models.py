from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=10)
    # 닉네임 설정 / 중복 안되게
    nickname = models.CharField(max_length=20, unique=True)
    birthday = models.DateField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

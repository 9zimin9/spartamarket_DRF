from django.conf import settings
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="products/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작가라는 필드(글과 연관, on_delete 속성값은 참조하고 있는 값을 어떻게 할건지 결정, CASCADE 연쇄적으로 삭제)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.title

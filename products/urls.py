from django.urls import path
from . import views


urlpatterns = [
    path(
        "", views.ProductListAPIView.as_view(), name="product_create_list"
    ),  # 상품 등록 및 목록조회
    path(
        "<int:pk>/", views.ProductDetailAPIView.as_view(), name="product_detail"
    ),  # 상품 수정 및 삭제
]

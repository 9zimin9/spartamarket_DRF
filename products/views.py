from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


# 상품 목록 조회 (GET) 및 등록 (POST)
class ProductListAPIView(APIView):
    # 유저만 접근 가능
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                author=request.user
            )  # 빈괄호가 아닌 author를 요청한 사용자로 지정
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 상품 수정(put) 및 삭제(DELETE)
class ProductDetailAPIView(APIView):
    # 유저만 접근 가능
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ProductSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

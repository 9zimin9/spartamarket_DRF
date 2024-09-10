from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


# 상품 목록 조회 (GET) 및 등록 (POST)
class ProductListAPIView(APIView):
    # 유저만 접근 가능

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"error": "로그인해주세요."}, status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                author=request.user
            )  # 빈괄호가 아닌 author를 요청한 사용자로 지정
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # 인증된 사용자 아닌경우 401에러


# 상품 수정(put) 및 삭제(DELETE)
class ProductDetailAPIView(APIView):
    # 유저만 접근 가능
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def put(self, request, pk):
        product = self.get_object(pk)
        # 요청한 사람이 상품 작성자인지 확인 (수정 시에도 필요-추가)
        if request.user != product.author:
            return Response(
                {"error": "수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        # 요청한 사람이 상품 작성자인지 확인( 삭제 시에도 필요- 추가)
        if request.user != product.author:
            return Response(
                {"error": "삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

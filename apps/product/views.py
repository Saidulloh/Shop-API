from rest_framework import generics,filters
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend

from apps.product.serializers import *
from apps.product.permissions import *
from apps.product.models import Product


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [SearchFilter, OrderingFilter]
    # filter_fields = [
    #             'price',
    #             ]               # filter
    # search_fields = [
    #         'title',
    #         ]                    # Поиск
    # ordering_fields = [
    #             'price',
    #             'category',
    #             'price',
    #             ]                # сортировка
    def get(self, request):
        c = Product.objects.filter(user=request.user)
        return Response(ProductSerializer(c, many=True).data)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
    permission_classes = [IsOwner or IsAdminUser]


class ProductDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwner or IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductCreateAPiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwner or IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
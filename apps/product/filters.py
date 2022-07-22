from django_filters import rest_framework as filters
from rest_framework.response import Response
from .models import Product


from rest_framework.pagination import PageNumberPagination

class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
    pass

class ProductFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name',lookup_expr='in')
    category = CharFilterInFilter(field_name='category__title',lookup_expr='in')

    class Meta:
        model = Product
        fields = ['name', 'category']
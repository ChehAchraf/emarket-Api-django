import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.CharFilter(field_name='name',lookup_expr="icontains")
    min_price = django_filters.NumberFilter(field_name="price" or 0 , lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price" or 100000 , lookup_expr="lte")
    class Meta:
        model = Product
        fields = ['Category','price','brand','keyword','min_price','max_price']
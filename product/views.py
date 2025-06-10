from django.shortcuts import render , get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.


@api_view(['GET'])
def get_all_products(request):
    filterset = ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    resPage = 1
    paginator = PageNumberPagination()
    paginator.page_size = resPage
    query_set = paginator.paginate_queryset(filterset.qs,request)
    serializer = ProductSerializer(query_set, many=True)
    return Response({"products": serializer.data})


@api_view(['GET'])
def get_product_by_id(request, pk):
    product = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(product,many=False)
    return Response({'Product':serializer.data})
    
from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.get_all_products,name="products"),
    path('product/<str:pk>', views.get_product_by_id,name="single_product")
]
from rest_framework import serializers
from .models import Product



## start the srealizing 

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Product
        fields = "__all__"
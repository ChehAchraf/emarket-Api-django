from rest_framework import serializers
from .models import Product



# start the srealizing 

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Product
        # tell the serializer which data we wanna receive 🙂
        fields = ['name','brand','price']
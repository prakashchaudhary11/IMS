from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['email','password']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductType
        fields ='__all__'
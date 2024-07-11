from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Product,ProductType
from .serializer import *
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


# Create your views here.

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email,password=password)

    if user == None:
        return Response('Invalid credintials')
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)

@api_view(['POST'])
def register(request):
    password1 = request.data.get('password')
    hash_password = make_password(password1)
    request.data['password'] = hash_password

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data created')
    else:
        return Response(serializer.errors)


class ProductTypeView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductApiView(GenericAPIView):
    

    # def get(self,request):
        
    #     product_obj = Product.objects.all()
    #     serializer = ProductSerializer(product_obj,many=True)
    #     return Response(serializer.data)
    
    # def post(self,request):
    #     serializer = ProductSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response('Data created')
    #     else:
    #         return Response(serializer.errors)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get(self,request):
        product_obj = self.get_queryset()
        serializer = self.serializer_class(product_obj,many=True)
        return Response(serializer.data)   
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created')
        else:
            return Response(serializer.errors)
        

class ProductDetailsApiView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,pk):
        try:
            product_objs = Product.objects.get(id=pk)
        except:
            return Response('Data not found')
        serializer = self.serializer_class(product_objs)
        return Response(serializer.data)
        
    def put(self,request,pk):
        try:
            product_objs = Product.objects.get(id=pk)
        except:
            return Response('Data not found')
        serializer = self.serializer_class(product_objs,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response('Data updated')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            product_objs = Product.objects.get(id=pk)
        except:
            return Response('Data not found')
        product_objs.delete()
        return Response('Data deleted')
    


            



from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category,Product,File
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer,ProductSerializer,FileSerializer

# Create your views here.
class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        print(request.auth)
        print(request.user)
        products = Product.objects.all()
        serializer = ProductSerializer(products,many = True,context={'request':request}) 
        return Response(serializer.data) 
class ProductDetailView(APIView):

    def get(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product,context={'request': request})
        return Response(serializer.data)
class CategoryListView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many =True, context={'request':request})
        return Response(serializer.data)
class CategoryDetailView(APIView):
    def get(self,request,pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category,context={'request': request})
        return Response(serializer.data)
class FileDetailView(APIView):
    def get(self,request,products_id,pk):
        try:
            
            files1 = File.objects.get(pk=pk,products_id=products_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(files1,context={'request': request})
        return Response(serializer.data)   
       
class FileListView(APIView):
    def get(self,request,products_id):
        file = File.objects.filter(products_id=products_id)
        serializer = FileSerializer(file,many =True, context={'request':request})
        return Response(serializer.data)
from django.shortcuts import render
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Product

# Create your views here.
from .serializers import ProductSerializer


class ProductApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):
        product=Product.object.filter(product=request.product.name)
        serializer=ProductSerializer(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        data={
            'price':request.data.get('price'),
            'image':request.data.get('image'),
            'name':request.product.name

        }

        serializer=ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,product_name,*args,**kwargs):
        product=self.get_object(product_name,request.product)
        if not product:
            return Response({"resp":"object not exist"},
                            status=status.HTTP_400_BAD_REQUEST)





from django.shortcuts import render
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from WhiteMarket.apps.products.models import Product, ProductCategory 
from WhiteMarket.apps.products.serializers import ProductSerializer, ProductCategorySerializer 
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle

# Create your views here.
class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 
 
class ProductCategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'productcategory-list'
    filter_fields = (
        'name',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        )


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'productcategory-detail'
    filter_fields = (
        'name',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        ) 

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-list'
    filter_fields = (
        'title',
        'category',
        )    
    search_fields = (
        '^title',
        '^description',
        )
    ordering_fields = (
        'created',
        'price',
        )
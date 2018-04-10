from django.shortcuts import render
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from WhiteMarket.apps.products.models import Product 
from WhiteMarket.apps.products.serializers import ProductSerializer 
from rest_framework.decorators import api_view

# Create your views here.
class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 
 
#Get Products === List Products
#Post Products === Create Product
@csrf_exempt 
@api_view(['GET', 'POST'])
def product_list(request): 
    if request.method == 'GET': 
        products = Product.objects.all() 
        products_serializer = ProductSerializer(products, many=True)
        return JSONResponse(products_serializer.data) 
 
    elif request.method == 'POST': 
        product_data = JSONParser().parse(request) 
        product_serializer = ProductSerializer(data=product_data) 
        if product_serializer.is_valid(): 
            product_serializer.save() 
            return JSONResponse(product_serializer.data, \
                status=status.HTTP_201_CREATED) 
        return JSONResponse(product_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST) 


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data)
        elif request.method == 'PUT':
            product_serializer = ProductSerializer(product, data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data)
            return Response(product_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            product.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
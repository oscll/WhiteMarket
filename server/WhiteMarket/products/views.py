from django.shortcuts import render
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from products.models import Product 
from products.serializers import ProductSerializer 
from django.contrib.gis.geoip2 import GeoIP2

# Create your views here.
class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 
 
#Get Products === List Products
#Post Products === Create Product
@csrf_exempt 
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

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    '''
    g = GeoIP2()
    return JSONResponse(g.city(get_client_ip(request)))
    '''
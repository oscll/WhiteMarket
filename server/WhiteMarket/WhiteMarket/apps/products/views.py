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
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from django.db import connection
from WhiteMarket import custompermission
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs)

 
class ProductCategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'productcategory-list'


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'productcategory-detail'


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )

    def get(self, request, pk):
        pk = self.kwargs.get('pk', None)
        obj = get_object_or_404(Product, pk=pk)
        obj.total_views += 1
        obj.save()
        return Response(ProductSerializer(obj, context={'request': self.request}).data)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user, total_views=0)

class ProductList(generics.ListCreateAPIView):

    def get_queryset(self):
        request = self.request
        if request.query_params.__contains__('latitude') & request.query_params.__contains__('longitude') & request.query_params.__contains__('distance'):
            latitude = request.query_params['latitude']
            longitude = request.query_params['longitude']
            radius = request.query_params['distance']
            radius = float(radius)

            """psql   "SELECT p.id, (6367*acos(cos(radians(38.829402))*cos(radians(latitude))*cos(radians(longitude)-radians(-0.610952)) +sin(radians(38.829402))*sin(radians(latitude)))) AS distance FROM products_product AS p INNER JOIN user_user AS u ON u.id = p.owner_id WHERE (6367*acos(cos(radians(38.829402))*cos(radians(latitude))*cos(radians(longitude)-radians(-0.610952)) +sin(radians(38.829402))*sin(radians(latitude)))) < 5.00000 ORDER BY distance ;" """
            query = """SELECT p.id, (6367*acos(cos(radians(%2f)) *cos(radians(latitude))*cos(radians(longitude)-radians(%2f)) +sin(radians(%2f))*sin(radians(latitude)))) AS distance FROM products_product AS p INNER JOIN user_user AS u ON u.id = p.owner_id WHERE (6367*acos(cos(radians(%2f)) *cos(radians(latitude))*cos(radians(longitude)-radians(%2f)) +sin(radians(%2f))*sin(radians(latitude)))) < %2f ORDER BY distance """ % (
                float(latitude),
                float(longitude),
                float(latitude),
                float(latitude),
                float(longitude),
                float(latitude),
                radius
            )
            ids = [p.id for p in Product.objects.raw(query)]
            return Product.objects.filter(id__in=ids)
        else:
            return Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-list'
    filter_fields = (
        'title',
        'category',
        'owner',
        'state',
        )
    search_fields = (
        'title',
        'description',
        )
    ordering_fields = (
        'created',
        'price',
        'total_views',
        'total_likes',
        )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, total_views=0)


class ProductLike(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-like'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        if request.user in obj.users_like.all():
            obj.users_like.remove(request.user)
            return Response(ProductSerializer(obj, context={'request': self.request}).data)
        else:
            obj.users_like.add(request.user)
            return Response(ProductSerializer(obj, context={'request': self.request}).data)


class ProductLiked(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-liked'
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        return Product.objects.filter(users_like__in=[self.request.user])

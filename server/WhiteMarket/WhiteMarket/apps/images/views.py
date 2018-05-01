from django.shortcuts import render
from rest_framework import viewsets, filters
from WhiteMarket.apps.images.serializers import ImageSerializer
from WhiteMarket.apps.images.models import Image
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.http import HttpResponse 
from rest_framework import generics
from rest_framework import permissions
from WhiteMarket import custompermission

# Create your views here.
class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 
 
class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    name = 'image-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        )

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    name = 'image-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
        )

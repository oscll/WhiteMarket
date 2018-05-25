from WhiteMarket.apps.images.serializers import  ImageSerializer
from rest_framework import serializers
from WhiteMarket.apps.images.models import Image
from WhiteMarket.apps.user.models import User
from WhiteMarket.apps.user.serializers import  UserSerializer
from django.shortcuts import  get_object_or_404


class ImageRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Image.objects.all()

    def to_internal_value(self, data):
        image = get_object_or_404(Image, pk=data)

        return image

    def to_representation(self, value):
        return ImageSerializer(value).data

class UserRelatedField(serializers.RelatedField):
    def get_queryset(self):
        print('joder154')
        return User.objects.all()

    def to_internal_value(self, data):
        print('joder122')
        user = get_object_or_404(Image, id=data)
        print('joder124')
        return user

    def to_representation(self, value):
        print('joder123')
        return UserSerializer(value).data


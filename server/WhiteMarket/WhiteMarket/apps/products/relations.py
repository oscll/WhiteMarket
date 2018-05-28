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
        return User.objects.all()

    def to_internal_value(self, data):
        user = get_object_or_404(User, id=data)
        return user

    def to_representation(self, value):
        return UserSerializer(value).data


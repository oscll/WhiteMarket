from rest_framework import serializers
from WhiteMarket.apps.images.models import Image
from WhiteMarket.apps.user.models import User

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Image
        fields = ('pk', 'image', 'thumbnail','owner',)
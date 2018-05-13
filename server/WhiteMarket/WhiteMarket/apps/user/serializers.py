from rest_framework import serializers
from WhiteMarket.apps.user.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'latitude', 'longitude')

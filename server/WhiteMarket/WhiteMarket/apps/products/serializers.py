from rest_framework import serializers 
from WhiteMarket.apps.products.models import Product , ProductCategory
from WhiteMarket.apps.user.models import User
 
 
 
class ProductSerializer(serializers.ModelSerializer): 
    category = serializers.SlugRelatedField(queryset=ProductCategory.objects.all(),
        slug_field='name')
    latitude = serializers.ReadOnlyField(source='owner.latitude')
    longitude = serializers.ReadOnlyField(source='owner.latitude')
    owner = serializers.ReadOnlyField(source='owner.email')
 
    class Meta:
        model = Product
        fields = (
            'pk',
            'created',
            'description',
            'img',
            'price',
            'discount',
            'category',
            'latitude',
            'longitude',
            'owner',
        )


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = (
            'pk',
            'name',
        )
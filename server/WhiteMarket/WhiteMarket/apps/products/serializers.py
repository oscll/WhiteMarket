from rest_framework import serializers 
from WhiteMarket.apps.products.models import Product , ProductCategory
from .relations import ImageRelatedField, UserRelatedField

 
 
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=ProductCategory.objects.all(),
        slug_field='name')
    latitude = serializers.ReadOnlyField(source='owner.latitude')
    longitude = serializers.ReadOnlyField(source='owner.latitude')
    # owner = serializers.ReadOnlyField(source='owner.email')
    owner = UserRelatedField(many=False)
    favorited = serializers.SerializerMethodField()
    images = ImageRelatedField(many=True)

    class Meta:
        model = Product
        fields = (
            'pk',
            'created',
            'title',
            'description',
            'images',
            'price',
            'state',
            'stock',
            'category',
            'latitude',
            'longitude',
            'owner',
            'total_likes',
            'total_views',
            'favorited',
        )

    def get_favorited(self, instance):
        request = self.context.get('request', None)
        if request is None:
            return False
        if not request.user.is_authenticated:
            return False
        if request.user in instance.users_like.all():
            return True
        return False


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = (
            'pk',
            'name',
        )
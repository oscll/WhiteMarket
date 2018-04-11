from rest_framework import serializers 
from WhiteMarket.apps.products.models import Product , ProductCategory
from WhiteMarket.apps.user.models import User
 
 
 
class ProductSerializer(serializers.Serializer): 
    pk = serializers.IntegerField(read_only=True) 
    created = serializers.DateTimeField()
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=250)
    img = serializers.CharField(max_length=250)
    price = serializers.DecimalField(max_digits=30, decimal_places=2)
    discount = serializers.IntegerField()
    category = serializers.SlugRelatedField(queryset=ProductCategory.objects.all(),
        slug_field='name')
    owner = serializers.ReadOnlyField(source='owner.username,owner.latitude, owner.longitude')
 
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
            'owner',
        )

    def create(self, validated_data): 
        return Product.objects.create(**validated_data) 
 
    def update(self, instance, validated_data): 
        instance.created = validated_data.get('created', instance.created)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.img = validated_data.get('img', instance.img)
        instance.price = validated_data.get('price', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.save() 
        return instance 

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = (
            'pk',
            'name',
        )
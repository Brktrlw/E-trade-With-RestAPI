from rest_framework import serializers
from FavoritesApp.models import ModelFavorite
from ProductsApp.api.serializers import ProductsSerializer
from UserApp.api.serializers import UserSerializer
from ProductsApp.models import ModelProduct

class FavoriteSerializer(serializers.ModelSerializer):
    product=ProductsSerializer()
    user=UserSerializer()
    class Meta:
        model  =ModelFavorite
        fields =("user","product")

class CreateFavoriteSerializer(serializers.ModelSerializer):
    productSlug=serializers.CharField(source="product.slug")

    class Meta:
        model = ModelFavorite
        fields=("productSlug",)

    def create(self, validated_data):
        product=ModelProduct.objects.get(slug=validated_data.get("product").get("slug"))
        return ModelFavorite.objects.create(product=product,user=validated_data.get("user"))

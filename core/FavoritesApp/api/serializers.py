from rest_framework import serializers
from FavoritesApp.models import ModelFavorite
from ProductsApp.api.serializers import ProductsSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    product=ProductsSerializer()
    class Meta:
        model  =ModelFavorite
        fields =("user","product")
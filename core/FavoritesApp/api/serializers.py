from rest_framework import serializers
from FavoritesApp.models import ModelFavorite
from ProductsApp.api.serializers import ProductsSerializer
from UserApp.api.serializers import UserSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    product=ProductsSerializer()
    user=UserSerializer()
    class Meta:
        model  =ModelFavorite
        fields =("user","product")
from rest_framework import serializers
from FavoritesApp.models import ModelFavorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model  =ModelFavorite
        fields =("product",)
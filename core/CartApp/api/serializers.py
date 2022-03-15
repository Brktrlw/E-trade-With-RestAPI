from rest_framework import serializers
from ProductsApp.models import ModelProduct
from CartApp.models import ModelCart,ModelCartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ModelCartItem
        fields = ("amount",)

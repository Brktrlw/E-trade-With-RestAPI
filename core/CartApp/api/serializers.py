from rest_framework import serializers
from CartApp.models import ModelCartItem
from ProductsApp.api.serializers import ProductsSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ModelCartItem
        fields = ("amount",)

class CartItemUpdateSerializer(serializers.ModelSerializer):
    slug=serializers.CharField(help_text="Ürün Slug")

    class Meta:
        model = ModelCartItem
        fields=("amount","slug")


class CartListSerializer(serializers.ModelSerializer):
    product=ProductsSerializer()
    class Meta:
        model  = ModelCartItem
        fields = ("product","amount")
from rest_framework import serializers
from CartApp.models import ModelCartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ModelCartItem
        fields = ("amount",)

class CartItemUpdateSerializer(serializers.ModelSerializer):
    slug=serializers.CharField(help_text="Ürün Slug")

    class Meta:
        model = ModelCartItem
        fields=("amount","slug")


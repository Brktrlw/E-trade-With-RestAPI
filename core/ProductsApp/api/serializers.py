from rest_framework import serializers
from ProductsApp.models import ModelProduct


class AllProductsSerializer(serializers.ModelSerializer):
    # THIS CLASS JUST FOR TEST, IT IS NOT FOR PROD.
    class Meta:
        model = ModelProduct
        fields=["name","description","category","slug","image","price"]

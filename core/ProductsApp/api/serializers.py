from rest_framework import serializers
from ProductsApp.models import ModelProduct

class AllProductsSerializer(serializers.ModelSerializer):
    # THIS CLASS JUST FOR TEST, IT IS NOT FOR PROD.
    def get_image(self,obj):
        return obj.image.url

    class Meta:
        model = ModelProduct
        fields=["name","description","categories","slug","image","price"]

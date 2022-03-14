from rest_framework import serializers
from ProductsApp.models import ModelProduct,ModelProductCategory

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelProductCategory
        fields=("name","slug")

class ProductsSerializer(serializers.ModelSerializer):
    image=serializers.SerializerMethodField()
    url=serializers.HyperlinkedIdentityField(view_name="products:url_productDetail",lookup_field="slug")
    category=CategorySerializer(many=True)

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = ModelProduct
        fields=["name","description","url","slug","image","price","category"]

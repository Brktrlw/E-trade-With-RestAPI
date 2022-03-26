from rest_framework import serializers
from ProductsApp.models import ModelProduct,ModelProductCategory
from SellerApp.api.serializers import SellerSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelProductCategory
        fields=("name","slug")


class ProductsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)
    url       = serializers.HyperlinkedIdentityField(view_name="products:url_productDetail",lookup_field="slug",read_only=True)
    category  = CategorySerializer(many=True)
    seller    = SellerSerializer()

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None

    class Meta:
        model = ModelProduct
        fields=["name","description","url","slug","shipping","image_url","price","category","seller"]

class CreateUpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelProduct
        fields=["name","description","image","price","category","draft"]


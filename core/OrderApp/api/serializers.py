from rest_framework import serializers
from OrderApp.models import ModelOrder,ModelOrderItems
from UserApp.models import ModelAddress

class OrderSerializer(serializers.ModelSerializer):
    addressId=serializers.CharField(source="address.unique_id")

    class Meta:
        model  = ModelOrder
        fields = ("addressId",)

    def create(self, validated_data):
        address=ModelAddress.objects.get(unique_id=validated_data.get("address").get("unique_id"))
        return ModelOrder.objects.create(address=address,user=validated_data.get("user"))











from rest_framework import serializers
from OrderApp.models import ModelOrder,ModelOrderItems
from UserApp.models import ModelAddress
from UserApp.api.serializers import AddressSerializer
from ProductsApp.api.serializers import ProductsSerializer
import json


with open('fixtures/cardMonth.json') as f:
    months = json.load(f)
months = [(k, v) for k, v in months.items()]

with open('fixtures/cardYear.json') as file:
    years = json.load(file)
years = [(key, value) for key, value in years.items()]

class CreditCardSerializer(serializers.Serializer):
    firstName  = serializers.CharField(max_length=200,required=True)
    lastName   = serializers.CharField(max_length=200,required=True)
    cardNumber = serializers.CharField(max_length=16,required=True)
    CVV        = serializers.CharField(max_length=4,required=True)
    month      = serializers.ChoiceField(required=True,choices=months)
    year       = serializers.ChoiceField(required=True,choices=years)

class OrderSerializer(serializers.ModelSerializer):
    addressId = serializers.CharField(source="address.unique_id")
    payment   = CreditCardSerializer(write_only=True)

    class Meta:
        model  = ModelOrder
        fields = ("addressId","payment")

    def create(self, validated_data):
        address=ModelAddress.objects.get(unique_id=validated_data.get("address").get("unique_id"))
        return ModelOrder.objects.create(address=address,user=validated_data.get("user"))


class OrderListSerializer(serializers.ModelSerializer):
    address=AddressSerializer()
    class Meta:
        model = ModelOrder
        fields=("createdDate","address","unique_id")


class OrderItemListSerializer(serializers.ModelSerializer):
    item=ProductsSerializer()

    class Meta:
        model = ModelOrderItems
        fields=("item","amount","price")








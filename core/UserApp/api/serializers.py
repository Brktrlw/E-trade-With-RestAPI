from rest_framework import serializers
from UserApp.models import ModelUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ModelUser
        fields = ("username","first_name","last_name")

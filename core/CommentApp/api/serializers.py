from rest_framework import serializers
from CommentApp.models import ModelComment
from UserApp.api.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    def get_url(self,obj):
        return obj.product.slug

    user=UserSerializer()
    class Meta:
        model=ModelComment
        fields=("user","comment","url","createdDate","modifiedDate")


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ModelComment
        fields = ("comment",)


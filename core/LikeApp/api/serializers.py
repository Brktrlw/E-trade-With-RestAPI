from rest_framework import serializers
from LikeApp.models import CommentLikeModel
from UserApp.api.serializers import UserSerializer

class CommentLikesSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=CommentLikeModel
        fields=("user",)



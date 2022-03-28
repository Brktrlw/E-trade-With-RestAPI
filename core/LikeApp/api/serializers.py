from django.http import JsonResponse
from rest_framework import serializers
from LikeApp.models import CommentLikeModel
from UserApp.api.serializers import UserSerializer
from CommentApp.models import ModelComment


class CommentLikesSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=CommentLikeModel
        fields=("user",)


class CreateDeleteCommentLikeSerializer(serializers.ModelSerializer):
    unique_id = serializers.CharField(source="comment.unique_id")
    class Meta:
        model=CommentLikeModel
        fields=("unique_id",)

    def create(self, validated_data):
        unique_id=validated_data.get("comment").get("unique_id")
        comment=ModelComment.objects.get(unique_id=unique_id)
        likeOBJ=CommentLikeModel.objects.filter(user=validated_data.get("user"),comment=comment)
        if likeOBJ.exists():
            return validated_data
        return CommentLikeModel.objects.create(comment=comment,user=validated_data.get("user"))



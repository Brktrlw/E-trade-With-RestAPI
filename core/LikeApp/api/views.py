from LikeApp.models import CommentLikeModel
from rest_framework.generics import ListAPIView
from .serializers import CommentLikesSerializer

class ListCommentLikes(ListAPIView):
    serializer_class = CommentLikesSerializer

    def get_queryset(self):
        return CommentLikeModel.objects.filter(comment__unique_id=self.kwargs.get("unique_id"))




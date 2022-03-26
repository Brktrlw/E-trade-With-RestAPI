from LikeApp.models import CommentLikeModel
from rest_framework.generics import ListAPIView


class ListCommentLikes(ListAPIView):

    serializer_class = ""

    def get_queryset(self):
        return CommentLikeModel.objects.filter()




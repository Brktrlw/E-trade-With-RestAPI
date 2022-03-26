from LikeApp.models import CommentLikeModel
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import CommentLikesSerializer,CreateCommentLikeSerializer
from rest_framework.permissions import IsAuthenticated

class ListCommentLikesAPIView(ListAPIView):
    serializer_class = CommentLikesSerializer

    def get_queryset(self):
        return CommentLikeModel.objects.filter(comment__unique_id=self.kwargs.get("unique_id"))


class CreateCommentLikeAPIView(CreateAPIView):
    serializer_class = CreateCommentLikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


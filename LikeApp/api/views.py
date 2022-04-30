from LikeApp.models import CommentLikeModel
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from .serializers import CommentLikesSerializer,CreateDeleteCommentLikeSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .paginations import CommentLikePagination


class ListCommentLikesAPIView(ListAPIView):
    serializer_class = CommentLikesSerializer
    pagination_class = CommentLikePagination
    def get_queryset(self):
        return CommentLikeModel.objects.filter(comment__unique_id=self.kwargs.get("unique_id"))


class CreateCommentLikeAPIView(CreateAPIView):
    serializer_class = CreateDeleteCommentLikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteCommentLikeAPIView(DestroyAPIView):
    serializer_class = CreateDeleteCommentLikeSerializer
    permission_classes = [IsOwner]
    queryset = CommentLikeModel.objects.all()
    lookup_field = "pk"


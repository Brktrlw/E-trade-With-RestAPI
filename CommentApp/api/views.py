from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404,DestroyAPIView,UpdateAPIView
from .serializers import CommentSerializer,CreateCommentSerializer
from CommentApp.models import ModelComment
from .paginations import CommentPagination
from ProductsApp.models import ModelProduct
from .permissions import IsOwner,IsAnyOrder
from .throttles import CommentThrottle


class ListCommentsAPIView(ListAPIView):
    pagination_class = CommentPagination
    queryset         = ModelComment.objects.all()
    serializer_class = CommentSerializer


class CreateCommentAPIView(CreateAPIView):
    serializer_class   = CreateCommentSerializer
    queryset           = ModelComment.objects.all()
    permission_classes = [IsAnyOrder]
    throttle_classes   = [CommentThrottle]

    def perform_create(self, serializer):
        product=get_object_or_404(ModelProduct,slug=self.kwargs.get("slug"))
        serializer.save(user=self.request.user,product=product)


class DeleteCommentAPIView(DestroyAPIView):
    queryset           = ModelComment.objects.all()
    serializer_class   = CommentSerializer
    lookup_field       = "unique_id"
    permission_classes = [IsOwner]


class UpdateCommentAPIView(UpdateAPIView):
    queryset           = ModelComment.objects.all()
    serializer_class   = CreateCommentSerializer
    lookup_field       = "unique_id"
    permission_classes = [IsOwner]
    throttle_classes   = [CommentThrottle]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
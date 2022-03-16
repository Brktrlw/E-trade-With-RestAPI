from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404
from .serializers import CommentSerializer,CreateCommentSerializer
from CommentApp.models import ModelComment
from .paginations import CommentPagination
from ProductsApp.models import ModelProduct
from rest_framework.permissions import IsAuthenticated


class ListCommentsView(ListAPIView):
    pagination_class = CommentPagination
    queryset         = ModelComment.objects.all()
    serializer_class = CommentSerializer


class CreateCommentView(CreateAPIView):
    serializer_class   = CreateCommentSerializer
    queryset           = ModelComment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        product=get_object_or_404(ModelProduct,slug=self.kwargs.get("slug"))
        serializer.save(user=self.request.user,product=product)





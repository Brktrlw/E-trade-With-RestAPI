from rest_framework.generics import ListAPIView
from .serializers import CommentSerializer
from CommentApp.models import ModelComment



class ListCommentsView(ListAPIView):
    queryset = ModelComment.objects.all()
    serializer_class = CommentSerializer



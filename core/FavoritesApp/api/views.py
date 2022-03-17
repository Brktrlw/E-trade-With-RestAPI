from rest_framework.generics import ListAPIView
from FavoritesApp.models import ModelFavorite
from .serializers import FavoriteSerializer
from rest_framework.permissions import IsAuthenticated
from .paginations import FavoritePagination

class ListFavoritesView(ListAPIView):
    serializer_class   = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    pagination_class   = FavoritePagination
    
    def get_queryset(self):
        return ModelFavorite.objects.filter(user=self.request.user)
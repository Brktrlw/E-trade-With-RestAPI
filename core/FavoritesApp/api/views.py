from rest_framework.generics import ListAPIView
from FavoritesApp.models import ModelFavorite
from .serializers import FavoriteSerializer

class ListFavoritesView(ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return ModelFavorite.objects.filter(user=self.request.user)
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404,DestroyAPIView
from FavoritesApp.models import ModelFavorite
from .serializers import FavoriteSerializer,CreateFavoriteSerializer
from rest_framework.permissions import IsAuthenticated
from .paginations import FavoritePagination
from ProductsApp.models import ModelProduct
from .throttles import FavoriteThrottle

class ListFavoritesView(ListAPIView):
    serializer_class   = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    pagination_class   = FavoritePagination

    def get_queryset(self):
        return ModelFavorite.objects.filter(user=self.request.user)


class AddFavoriteView(CreateAPIView):
    queryset           = ModelFavorite.objects.all()
    serializer_class   = CreateFavoriteSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes   = [FavoriteThrottle]

    def perform_create(self, serializer):
        product = get_object_or_404(ModelProduct,slug=serializer.validated_data.get("product").get("slug"))
        favOBJ  = ModelFavorite.objects.filter(user=self.request.user, product=product)
        if not favOBJ:
            serializer.save(user=self.request.user)


class DeleteFavoriteView(DestroyAPIView):
    queryset           = ModelFavorite.objects.all()
    serializer_class   = CreateFavoriteSerializer
    lookup_field       = "pk"
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return ModelFavorite.objects.get(user=self.request.user)




from rest_framework.generics import ListAPIView
from ProductsApp.models import ModelProduct
from .serializers import AllProductsSerializer

class AllProductListView(ListAPIView):
    # THIS CLASS JUST FOR TEST, IT IS NOT FOR PROD.
    serializer_class = AllProductsSerializer

    def get_queryset(self):
        return ModelProduct.objects.filter(draft=False).order_by("?")

class ListProductByCategory(ListAPIView):
    pass

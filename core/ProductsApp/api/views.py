from rest_framework.generics import ListAPIView
from ProductsApp.models import ModelProduct,ModelProductCategory
from .serializers import ProductsSerializer

class AllProductListView(ListAPIView):
    # THIS CLASS JUST FOR TEST, IT IS NOT FOR PROD.
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return ModelProduct.objects.filter(draft=False).order_by("?")

class ListProductByCategory(ListAPIView):
    serializer_class = ProductsSerializer
    lookup_field     = "slug"
    def get_queryset(self):
        return ModelProduct.objects.filter(draft=False,category__slug=self.kwargs.get("slug"))


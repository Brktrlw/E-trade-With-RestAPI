from rest_framework.generics import (
    ListAPIView,RetrieveAPIView,CreateAPIView,
    DestroyAPIView,RetrieveUpdateAPIView)
from ProductsApp.models import ModelProduct
from .serializers import ProductsSerializer,CreateUpdateProductSerializer


class AllProductListView(ListAPIView):
    # Lists all products randomly
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return ModelProduct.objects.filter(draft=False).order_by("?")

class ListProductByCategory(ListAPIView):
    # Lists products by category
    serializer_class = ProductsSerializer
    lookup_field     = "slug"
    def get_queryset(self):
        return ModelProduct.objects.filter(draft=False,category__slug=self.kwargs.get("slug"))

class DetailProductView(RetrieveAPIView):
    # List one product by it's slug
    queryset         = ModelProduct.objects.all()
    lookup_field     = "slug"
    serializer_class = ProductsSerializer


class CreateProductView(CreateAPIView):
    queryset         = ModelProduct.objects.all()
    serializer_class = CreateUpdateProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset         = ModelProduct.objects.all()
    serializer_class = ProductsSerializer
    lookup_field     = "slug"


class UpdateProductView(RetrieveUpdateAPIView):
    queryset         = ModelProduct.objects.all()
    serializer_class = CreateUpdateProductSerializer
    lookup_field     = "slug"






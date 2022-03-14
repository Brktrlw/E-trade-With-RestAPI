from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView)
from ProductsApp.models import ModelProduct
from .serializers import ProductsSerializer,CreateProductSerializer

class AllProductListView(ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return ModelProduct.objects.filter(draft=False).order_by("?")

class ListProductByCategory(ListAPIView):
    serializer_class = ProductsSerializer
    lookup_field     = "slug"
    def get_queryset(self):
        return ModelProduct.objects.filter(draft=False,category__slug=self.kwargs.get("slug"))

class DetailProductView(RetrieveAPIView):
    queryset         = ModelProduct.objects.all()
    lookup_field     = "slug"
    serializer_class = ProductsSerializer


class CreateProductView(CreateAPIView):
    queryset         = ModelProduct.objects.all()
    serializer_class = CreateProductSerializer








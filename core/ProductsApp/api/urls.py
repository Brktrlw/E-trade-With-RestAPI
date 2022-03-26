from django.urls import path
from .views import (AllProductListView,ListProductByCategory,
                    DetailProductView,CreateProductView,
                    DeleteProductView,UpdateProductView)


app_name="products"
urlpatterns = [
    path("all/",AllProductListView.as_view(),name="url_allProducts"),
    path("cat/<slug>",ListProductByCategory.as_view(),name="url_produtcsByCat"),
    path("detail/<slug>",DetailProductView.as_view(),name="url_productDetail"),

    # FOR CRUD
    path("create/",CreateProductView.as_view(),name="url_productCreate"),
    path("delete/<slug>",DeleteProductView.as_view(),name="url_productDelete"),
    path("update/<slug>",UpdateProductView.as_view(),name="url_productUpdate")
]

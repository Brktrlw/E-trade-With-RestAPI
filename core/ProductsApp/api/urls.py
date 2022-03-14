

from django.urls import path
from .views import AllProductListView,ListProductByCategory

app_name="products"
urlpatterns = [
    path("all/",AllProductListView.as_view(),name="url_allProducts"),
    path("cat/<slug>",ListProductByCategory.as_view(),name="url_produtcsByCat")
]

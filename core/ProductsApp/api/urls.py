

from django.urls import path
from .views import AllProductListView

app_name="products"
urlpatterns = [
    path("all/",AllProductListView.as_view(),name="url_allProducts")
]

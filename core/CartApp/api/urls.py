
from django.urls import path
from .views import AddProductToCartView,ReduceProductFromCartView

app_name="carts"
urlpatterns = [
    path("addtocart/<slug>",AddProductToCartView.as_view(),name="url_addToCart"),
    path("reducetocart/<slug>",ReduceProductFromCartView.as_view(),name="url_reduceToCart")
]

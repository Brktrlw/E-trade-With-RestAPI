
from django.urls import path
from .views import (AddProductToCartAPIView,ReduceProductFromCartAPIView,
                    DeleteProductFromCartAPIView,UpdateCartItemAmountAPIView,
                    ListCartAPIView)

app_name="carts"
urlpatterns = [
    path("addtocart/<slug>",AddProductToCartAPIView.as_view(),name="url_addToCart"),
    path("reducetocart/<slug>",ReduceProductFromCartAPIView.as_view(),name="url_reduceToCart"),
    path("deletetoproduct/<slug>",DeleteProductFromCartAPIView.as_view(),name="url_deletetoproduct"),
    path("updatecart/<slug>",UpdateCartItemAmountAPIView.as_view(),name="url_updatecart"),
    path("list/",ListCartAPIView.as_view(),name="url_listcart")

]

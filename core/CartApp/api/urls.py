
from django.urls import path
from .views import AddProductToCartAPIView,ReduceProductFromCartAPIView,DeleteProductFromCartAPIView,UpdateCartItemAmountAPIView

app_name="carts"
urlpatterns = [
    path("addtocart/<slug>",AddProductToCartAPIView.as_view(),name="url_addToCart"),
    path("reducetocart/<slug>",ReduceProductFromCartAPIView.as_view(),name="url_reduceToCart"),
    path("deletetoproduct/<slug>",DeleteProductFromCartAPIView.as_view(),name="url_deletetoproduct"),
    path("updatecart/<slug>",UpdateCartItemAmountAPIView.as_view(),name="url_updatecart")

]

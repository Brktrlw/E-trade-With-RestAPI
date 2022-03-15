
from django.urls import path
from .views import AddProductToCartView,ReduceProductFromCartView,DeleteProductFromCartView,UpdateCartItemAmountView

app_name="carts"
urlpatterns = [
    path("addtocart/<slug>",AddProductToCartView.as_view(),name="url_addToCart"),
    path("reducetocart/<slug>",ReduceProductFromCartView.as_view(),name="url_reduceToCart"),
    path("deletetoproduct/<slug>",DeleteProductFromCartView.as_view(),name="url_deletetoproduct"),
    path("updatecart/<slug>",UpdateCartItemAmountView.as_view(),name="url_updatecart")

]

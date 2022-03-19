
from django.urls import path
from .views import CreateOrderAPIView,ListOrdersAPIView


app_name="orders"
urlpatterns = [
    path("create/",CreateOrderAPIView.as_view(),name="url_createorder"),
    path("list/",ListOrdersAPIView.as_view(),name="url_listorder")
]


from django.urls import path
from .views import CreateOrderAPIView,ListOrdersAPIView,OrderItemsListAPIView


app_name="orders"
urlpatterns = [
    path("create/",CreateOrderAPIView.as_view(),name="url_createorder"),
    path("list/",ListOrdersAPIView.as_view(),name="url_listorder"),
    path("detail/<str:unique_id>",OrderItemsListAPIView.as_view(),name="url_listorderitems")
]

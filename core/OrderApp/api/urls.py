
from django.urls import path
from .views import CreateOrderAPIView


app_name="orders"
urlpatterns = [
    path("create/",CreateOrderAPIView.as_view(),name="url_createorder")
]

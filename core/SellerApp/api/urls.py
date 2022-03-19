
from django.urls import path
from .views import UpdateSellerProfileAPIView



app_name="sellers"
urlpatterns = [
    path("update/",UpdateSellerProfileAPIView.as_view(),name="url_updateseller")
]

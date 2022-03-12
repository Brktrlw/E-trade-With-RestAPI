

from django.urls import path
from .views import AllProductListView

urlpatterns = [
    path("all/",AllProductListView.as_view(),name="url_allProducts")
]

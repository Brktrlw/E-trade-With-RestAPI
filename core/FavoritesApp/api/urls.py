

from django.urls import path
from .views import ListFavoritesView

app_name="favorites"
urlpatterns = [
    path("list/",ListFavoritesView.as_view(),name="url_listfavorites")
]

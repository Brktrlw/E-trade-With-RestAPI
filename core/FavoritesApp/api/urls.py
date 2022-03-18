

from django.urls import path
from .views import ListFavoritesView,AddFavoriteView

app_name="favorites"
urlpatterns = [
    path("list/",ListFavoritesView.as_view(),name="url_listfavorites"),
    path("add/",AddFavoriteView.as_view(),name="url_addfavorite")
]

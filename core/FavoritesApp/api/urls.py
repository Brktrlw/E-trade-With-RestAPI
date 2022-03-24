

from django.urls import path
from .views import ListFavoritesView,AddFavoriteView,DeleteFavoriteView
from django.utils.translation import gettext as _


app_name="favorites"
urlpatterns = [
    path("list/",ListFavoritesView.as_view(),name="url_listfavorites"),
    path(_("add/"),AddFavoriteView.as_view(),name="url_addfavorite"),
    path("delete/<pk>",DeleteFavoriteView.as_view(),name="url_deletefavorite")
]

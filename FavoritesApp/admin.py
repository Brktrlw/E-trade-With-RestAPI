from django.contrib import admin
from FavoritesApp.models import ModelFavorite


@admin.register(ModelFavorite)
class AdminFavorite(admin.ModelAdmin):
    list_display       = ["user","product","createdDate"]
    list_display_links = ["user","product"]
    search_fields      = ["user"]
    list_filter        = ["product"]

    class Meta:
        model = ModelFavorite










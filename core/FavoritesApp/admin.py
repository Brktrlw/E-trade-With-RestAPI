from django.contrib import admin
from FavoritesApp.models import ModelFavorite


@admin.register(ModelFavorite)
class AdminProduct(admin.ModelAdmin):
    list_display       = ["user","product"]
    list_display_links = ["user","product"]
    search_fields      = ["user"]
    list_filter        = ["product"]

    class Meta:
        model = ModelFavorite










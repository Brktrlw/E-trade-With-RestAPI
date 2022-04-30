from django.contrib import admin
from .models import ModelCart,ModelCartItem


admin.site.register(ModelCart)

@admin.register(ModelCartItem)
class AdminCartItem(admin.ModelAdmin):
    list_display       = ["product","amount"]
    list_display_links = ["product","amount"]
    search_fields      = ["product"]
    list_filter        = ["product"]

    class Meta:
        model = ModelCartItem


from django.contrib import admin
from .models import ModelCart,ModelCartItem


admin.site.register(ModelCart)

@admin.register(ModelCartItem)
class AdminCartItem(admin.ModelAdmin):
    list_display       = ["item","amount"]
    list_display_links = ["item","amount"]
    search_fields      = ["item"]
    list_filter        = ["item"]

    class Meta:
        model = ModelCartItem


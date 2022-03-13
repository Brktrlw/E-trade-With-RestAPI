from django.contrib import admin
from .models import ModelProductCategory,ModelProduct

panelListForProduct=["name","slug"]

@admin.register(ModelProduct)
class AdminProduct(admin.ModelAdmin):
    list_display       = panelListForProduct + ["price","draft"]
    list_display_links = panelListForProduct
    search_fields      = panelListForProduct
    list_filter        = ["price"]
    list_editable      = ["draft"]
    readonly_fields    = ["slug"]

    class Meta:
        model = ModelProduct


@admin.register(ModelProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display    = ["id"]+panelListForProduct
    search_fields   = panelListForProduct
    readonly_fields = ["slug"]
    list_editable   = ["name"]

    class Meta:
        model = ModelProductCategory


from django.contrib import admin
from .models import ModelProductCategory,ModelProduct


@admin.register(ModelProduct)
class AdminProduct(admin.ModelAdmin):
    panelListForProduct=["name","slug"]
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

    class Meta:
        model = ModelProductCategory


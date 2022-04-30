from django.contrib import admin
from .models import ModelComment


@admin.register(ModelComment)
class AdminComment(admin.ModelAdmin):
    readonly_fields    = ["unique_id","createdDate","modifiedDate"]
    listForComment     = ["product","comment","createdDate","modifiedDate","unique_id"]
    list_display       = listForComment
    list_display_links = listForComment[0:1]
    search_fields      = ["product__name"]
    list_filter        = listForComment[0:1]

    class Meta:
        model = ModelComment



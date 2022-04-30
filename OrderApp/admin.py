from django.contrib import admin
from .models import ModelOrder,ModelOrderItems


@admin.register(ModelOrder)
class AdminOrder(admin.ModelAdmin):
    listForOrder       = ["unique_id","user","createdDate"]
    list_display       = listForOrder
    list_display_links = listForOrder
    search_fields      = ["user"]

    class Meta:
        model = ModelOrder


@admin.register(ModelOrderItems)
class AdminOrderItem(admin.ModelAdmin):
    listForOrder       = ["order","item","amount"]
    list_display       = listForOrder
    list_display_links = listForOrder

    class Meta:
        model = ModelOrderItems

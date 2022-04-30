from django.contrib import admin
from .models import ModelSeller

@admin.register(ModelSeller)
class SellerAdmin(admin.ModelAdmin):

    list_display       = ["user","companyName","phone"]
    search_fields      = ["user"]

    class Meta:
        model=ModelSeller
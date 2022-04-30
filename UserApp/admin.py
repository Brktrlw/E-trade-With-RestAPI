from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ModelUser,ModelAddress


@admin.register(ModelUser)
class CustomUserAdmin(UserAdmin):
    model        = ModelUser
    fieldsets    = UserAdmin.fieldsets +(
        ("Extra",{
            "fields":["avatar","address","isCustomer"]
        }),
    )


@admin.register(ModelAddress)
class AddressAdmin(admin.ModelAdmin):
    panelListForUser   = ["name","unique_id", "city","street"]
    list_display       = panelListForUser
    list_editable      = ["city"]
    search_fields      = ["name"]

    class Meta:
        model=ModelAddress

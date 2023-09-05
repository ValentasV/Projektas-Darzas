from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from vartotojai.models import Vartotojas


class VartotojasAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "phone", "email", "active", "admin")
    list_filter = ("first_name", "last_name", "active", "admin")
    fieldsets = (
        (None, {"fields": ["email", "password"]}),
        ("Personal Info", {"fields": ("first_name", "last_name", "phone")}),
        ("Permissions", {"fields": ["admin", "staff", "active"]}),
    )
    add_fieldsets = (
        (None, {
            "classes": ["wide"],
            "fields": ["first_name", "last_name", "phone", "email", "password1", "password2"],
        }),
    )
    search_fields = ["first_name", "email"]
    ordering = ["first_name"]
    filter_horizontal = []

admin.site.register(Vartotojas, VartotojasAdmin)

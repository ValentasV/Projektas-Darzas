from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from vartotojai.models import Vartotojas


class VartotojasAdmin(UserAdmin):
    list_display = ("vardas", "pavarde", "telefonas", "elektroninis_pastas", "active", "admin")
    list_filter = ("vardas", "pavarde", "active", "admin")
    fieldsets = (
        (None, {"fields": ["elektroninis_pastas", "password"]}),
        ("Personal Info", {"fields": ("vardas", "pavarde", "telefonas")}),
        ("Permissions", {"fields": ["admin", "staff", "active"]}),
    )
    add_fieldsets = (
        (None, {
            "classes": ["wide"],
            "fields": ["vardas", "pavarde", "telefonas", "elektroninis_pastas", "password1", "password2"],
        }),
    )
    search_fields = ["vardas", "elektroninis_pastas"]
    ordering = ["vardas"]
    filter_horizontal = []

admin.site.register(Vartotojas, VartotojasAdmin)

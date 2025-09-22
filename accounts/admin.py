from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "is_active", "is_staff", "is_superuser")
    search_fields = ("username",)
    ordering = ("id",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

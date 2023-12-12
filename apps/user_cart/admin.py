from django.contrib import admin
from .models import UserCart


class UserCartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "quantity")


admin.site.register(UserCart, UserCartAdmin)

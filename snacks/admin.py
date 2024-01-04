from django.contrib import admin
from .models import Snack


class SnackAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at", "updated_at")


admin.site.register(Snack, SnackAdmin)
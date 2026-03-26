from django.contrib import admin
from .models import SwapRequest, Swap

@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "from_user", "to_user", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("book__title", "from_user__username", "to_user__username")

@admin.register(Swap)
class SwapAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "owner", "borrower", "type", "status", "created_at")
    list_filter = ("status", "type")
    search_fields = ("book__title", "owner__username", "borrower__username")
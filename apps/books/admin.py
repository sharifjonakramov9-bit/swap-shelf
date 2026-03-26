from django.contrib import admin
from .models import Book, Genre

admin.site.register(Genre)
admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "owner", "status", "created_at")
    list_filter = ("status", "genre", "condition")
    search_fields = ("title", "author", "owner__username")
    ordering = ("-created_at",)
    list_select_related = ("owner", "genre")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)

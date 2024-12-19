from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'genre', 'category', 'publisher')
    search_fields = ('title', 'author__name', 'genre', 'publisher')
    list_filter = ('category', 'genre', 'year')
    ordering = ('title',)
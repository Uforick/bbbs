from django.contrib import admin

from bbbs.books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'description', 'genre')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Book, BookAdmin)

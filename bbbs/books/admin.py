from django.contrib import admin

from bbbs.books.models import Book, Tag


class BookTagInline(admin.TabularInline):
    model = Book.tag.through
    extra = 1
    min_num = 1
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'

    def has_delete_permission(self, request, obj):
        try:
            if obj.tag.count() == 1:
                return False
        except:
            pass
        return super().has_delete_permission(request, obj=obj)


class BookAdmin(admin.ModelAdmin):
    inlines = (BookTagInline,)
    list_display = ('title', 'author', 'year', 'genre')
    search_fields = ('title', 'author')
    list_filter = ('year', 'genre')
    ordering = ('title',)
    exclude = ('tag',)
    empty_value_display = '-пусто-'

    def get_tags(self, obj):
        qs = obj.list_tags()
        if qs:
            return list(qs)

    get_tags.short_description = 'Теги'

    
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Book, BookAdmin)

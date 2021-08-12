from django.contrib import admin

from bbbs.movies.forms import MovieAdminForm
from bbbs.movies.models import Movie, Tag


class MovieTagInline(admin.TabularInline):
    model = Movie.tag.through
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


class MovieAdmin(admin.ModelAdmin):
    form = MovieAdminForm
    inlines = (MovieTagInline,)
    list_display = ('title', 'info', 'link', 'get_tags')
    search_fields = ('title',)
    list_filter = ('tag', 'show_on_main_page')
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
admin.site.register(Movie, MovieAdmin)


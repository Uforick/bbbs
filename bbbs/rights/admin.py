from django.contrib import admin

from bbbs.rights.models import Right, Tag


class RightTagInline(admin.TabularInline):
    model = Right.tag.through
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


class RightTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('name',)}


class RightAdmin(admin.ModelAdmin):
    inlines = (RightTagInline,)
    list_display = ('title', 'color', 'get_tags')
    search_fields = ('title',)
    list_filter = ('title', 'color')
    exclude = ('tag',)

    def get_tags(self, obj):
        qs = obj.list_tags()
        if qs:
            return list(qs)

    get_tags.short_description = 'Теги'

admin.site.register(Right, RightAdmin)
admin.site.register(Tag, RightTagAdmin)

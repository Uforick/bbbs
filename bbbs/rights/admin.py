from django.contrib import admin

from bbbs.rights.models import Right, RightTag


class RightTagInline(admin.TabularInline):
    model = Right.tag.through
    raw_id_fields = ('righttag',)
    extra = 1
    min_num = 1


class RightTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('name',)}


class RightAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'tags_display')
    search_fields = ('title',)
    list_filter = ('title', 'color')
    exclude = ('tag',)
    inlines = (RightTagInline,)

    def tags_display(self, obj):
        return ", ".join([
            tag.name for tag in obj.tag.all()
        ])
    tags_display.short_description = 'Теги'


admin.site.register(Right, RightAdmin)
admin.site.register(RightTag, RightTagAdmin)

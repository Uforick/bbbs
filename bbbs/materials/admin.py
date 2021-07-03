from django.contrib import admin

from bbbs.materials.models import Material


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'imageUrl')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Material, MaterialAdmin)

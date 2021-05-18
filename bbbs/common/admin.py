from django.contrib import admin

from bbbs.common.models import City, Profile


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_primary')
    search_fields = ('name',)
    list_filter = ('name', 'is_primary')
    ordering = ('name',)
    empty_value_display = '-пусто-'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')
    search_fields = ('user', 'city')
    list_filter = ('user', 'city')
    ordering = ('user', 'city')
    empty_value_display = '-пусто-'


admin.site.register(City, CityAdmin)
admin.site.register(Profile, ProfileAdmin)

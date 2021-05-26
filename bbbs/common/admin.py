from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from bbbs.common.models import City, Profile
from bbbs.common.forms import ProfileAdminForm


User = get_user_model()


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_primary')
    search_fields = ('name',)
    list_filter = ('name', 'is_primary')
    ordering = ('name',)
    empty_value_display = '-пусто-'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ('user', 'city')
    search_fields = ('user', 'city')
    list_filter = ('user', 'city')
    ordering = ('user', 'city')
    empty_value_display = '-пусто-'


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    list_display = ('username', 'email', 'is_staff','is_active')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    ordering = ('username', 'email')
    empty_value_display = '-пусто-'


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(User, MyUserAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Profile, ProfileAdmin)

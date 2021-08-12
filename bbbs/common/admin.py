from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from bbbs.common.forms import ProfileAdminForm
from bbbs.common.models import City, Profile


User = get_user_model()


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_primary')
    search_fields = ('name',)
    list_filter = ('is_primary',)
    ordering = ('name',)
    empty_value_display = '-пусто-'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ('user', 'get_cities', 'role')
    search_fields = ('user', 'city')
    list_filter = ('user', 'city')
    ordering = ('user__username',)
    empty_value_display = '-пусто-'

    def get_cities(self, obj):
        qs = Profile.objects.filter(
            pk=obj.pk, city__isnull=False
            ).values_list('city__name', flat=True)
        if qs:
            return list(qs)

    get_cities.short_description = 'Города'


class ProfileInline(admin.TabularInline):
    model = Profile
    form = ProfileAdminForm
    extra = 1
    min_num = 1
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'
    

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    ordering = ('username', 'email')
    empty_value_display = '-пусто-'
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(User, MyUserAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Profile, ProfileAdmin)

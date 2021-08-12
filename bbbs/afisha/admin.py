from django.contrib import admin
from django.contrib.auth import get_user_model

from bbbs.afisha.forms import EventAdminForm
from bbbs.afisha.models import Event
from bbbs.common.models import Profile

User = get_user_model()


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ('title', 'city', 'contact', 'start_at', 'end_at')
    search_fields = ('title', 'city', 'contact', 'start_at', 'end_at')
    list_filter = ('title', 'city', 'contact', 'start_at', 'end_at')
    ordering = ('city', '-start_at')
    empty_value_display = '-пусто-'
    exclude = ('booked',)
    readonly_fields = ('get_taken_seats',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user_profile = Profile.objects.get(user=request.user)
        if user_profile.role == Profile.PermissionChoice.REGION_MODERATOR:
            return qs.filter(city__in=user_profile.user_cities)
        return qs

    def get_taken_seats(self, obj):
        return obj.taken_seats

    get_taken_seats.short_description = 'Кол-во занятых мест'

admin.site.register(Event, EventAdmin)

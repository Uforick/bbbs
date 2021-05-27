from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth import get_user_model

from bbbs.afisha.models import Event, EventParticipant
from bbbs.common.models import Profile

User = get_user_model()


class MyEventChangeList(ChangeList):
    def get_queryset(self, request):
        qs = super(MyEventChangeList, self).get_queryset(request)
        user_profile = Profile.objects.get(user=request.user)
        # фильтруем выдачу для регионального модератора по городу
        if user_profile.role == 'REGION_MODERATOR':
            return qs.filter(city__in = user_profile.get_city)
        return qs


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'contact', 'start_at', 'end_at')
    search_fields = ('title', 'city', 'contact', 'start_at', 'end_at')
    list_filter = ('title', 'city', 'contact', 'start_at', 'end_at')
    ordering = ('city',)
    empty_value_display = '-пусто-'
    readonly_fields = ('taken_seats',)

    def get_changelist(self, request, **kwargs):
        return MyEventChangeList


admin.site.register(Event, EventAdmin)

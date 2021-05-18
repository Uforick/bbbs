from django.contrib import admin

from bbbs.afisha.models import Event, EventParticipant


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'contact', 'start_at', 'end_at')
    search_fields = ('title', 'city', 'contact', 'start_at', 'end_at')
    list_filter = ('title', 'city', 'contact', 'start_at', 'end_at')
    ordering = ('city',)
    empty_value_display = '-пусто-'


class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    search_fields = ('user', 'event')
    list_filter = ('user', 'event')
    ordering = ('user',)
    empty_value_display = '-пусто-'


admin.site.register(Event, EventAdmin)
admin.site.register(EventParticipant, EventParticipantAdmin)

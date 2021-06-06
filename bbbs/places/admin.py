from django.contrib import admin

from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'chosen', 'address', 'gender', 'age',
        'activity_type', 'description', 'link', 'get_tags', 'imageUrl'
    )
    search_fields = ('title', 'address', 'tag')
    list_filter = ('chosen', 'activity_type')
    empty_value_display = '-пусто-'

    def get_tags(self, obj):
        qs = Place.objects.filter(
            pk=obj.pk, tag__isnull=False
            ).values_list('tag__name', flat=True)
        if qs:
            return list(qs)

    get_tags.short_description = 'Теги'


admin.site.register(Place, PlaceAdmin)

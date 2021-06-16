from bbbs.common.models import Profile
from django.contrib import admin

from .models import Place, Tag
from bbbs.questions.admin import TagAdmin


class PlaceTagInline(admin.TabularInline):
    model = Place.tag.through
    extra = 1
    min_num = 1

    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'


class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'chosen', 'address', 'gender', 'age',
        'activity_type', 'description', 'link', 'get_tags', 'imageUrl'
    )
    search_fields = ('title', 'address', 'tag')
    list_filter = ('chosen', 'activity_type')
    empty_value_display = '-пусто-'
    exclude = ('tag',)
    inlines = (PlaceTagInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user_profile = Profile.objects.get(user=request.user)
        if user_profile.role == Profile.PermissionChoice.REGION_MODERATOR:
            return qs.filter(city__in=user_profile.user_cities)
        return qs

    def get_tags(self, obj):
        qs = obj.list_tags()
        if qs:
            return list(qs)

    get_tags.short_description = 'Теги'


admin.site.register(Tag, TagAdmin)
admin.site.register(Place, PlaceAdmin)

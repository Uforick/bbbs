from django.contrib import admin

from bbbs.videos.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'imageUrl', 'info', 'link',) # пока без 'tag'
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Video, VideoAdmin)

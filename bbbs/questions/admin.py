from django.contrib import admin

from .models import  Question, Tag


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question', 'answer','get_tags'
    )
    search_fields = ('question', 'answer', 'tag')
    list_filter = ('question', 'answer')
    empty_value_display = '-пусто-'

    def get_tags(self, obj):
        qs = obj.list_tags()
        if qs:
            return list(qs)

    get_tags.short_description = 'Теги'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    empty_value_display = '-пусто-'


admin.site.register(Tag, TagAdmin)
admin.site.register(Question, QuestionAdmin)
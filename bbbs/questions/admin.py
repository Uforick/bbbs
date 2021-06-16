from django.contrib import admin

from .models import Question, Tag


class QuestionTagInline(admin.TabularInline):
    model = Question.tag.through
    extra = 1
    min_num = 1

    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question', 'answer', 'get_tags'
    )
    search_fields = ('question', 'answer', 'tag')
    list_filter = ('question', 'answer')
    empty_value_display = '-пусто-'
    exclude = ('tag',)
    inlines = (QuestionTagInline,)

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
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Question, QuestionAdmin)

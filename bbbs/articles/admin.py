from django.contrib import admin

from bbbs.articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'link', 'text')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Article, ArticleAdmin)

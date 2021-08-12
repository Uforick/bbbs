from django.contrib import admin

from bbbs.articles.forms import ArticlesAdminForm
from bbbs.articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author',)
    ordering = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Article, ArticleAdmin)

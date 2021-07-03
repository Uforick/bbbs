from rest_framework import serializers

from bbbs.articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ("show_on_main_page",)

from rest_framework import generics

from bbbs.articles.models import Article
from bbbs.articles.serializers import ArticleSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

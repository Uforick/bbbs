from rest_framework import generics

from bbbs.movies.filters import MovieFilter
from bbbs.movies.models import Movie, Tag
from bbbs.movies.serializers import MovieSerializer, TagSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_class = MovieFilter


class MovieTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
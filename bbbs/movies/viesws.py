from rest_framework import generics

from bbbs.movies.models import Movie
from bbbs.movies.serializers import MovieSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

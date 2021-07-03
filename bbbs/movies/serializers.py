from rest_framework import serializers

from bbbs.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ("show_on_main_page",)

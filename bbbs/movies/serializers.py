from rest_framework import serializers

from bbbs.movies.models import Movie, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

        
class MovieSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        exclude = ("show_on_main_page",)

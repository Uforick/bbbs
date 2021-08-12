from rest_framework import serializers

from bbbs.videos.models import Tag, Video

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

        
class VideoSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Video
        exclude = ("show_on_main_page",)

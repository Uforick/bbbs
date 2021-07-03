from rest_framework import serializers

from bbbs.videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ("show_on_main_page",)

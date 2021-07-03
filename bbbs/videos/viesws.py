from rest_framework import generics

from bbbs.videos.models import Video
from bbbs.videos.serializers import VideoSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

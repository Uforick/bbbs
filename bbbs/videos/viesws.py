from rest_framework import generics

from bbbs.videos.models import Tag, Video
from bbbs.videos.serializers import TagSerializer, VideoSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
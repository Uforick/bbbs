from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import pagination

from .models import Place, Tag
from .serializers import PlaceListSerializer, PlaceSerializer, TagSerializer
from .generics import CreateUpdateAPIView
from bbbs.common.models import User


class PlaceList(generics.ListAPIView):
    serializer_class = PlaceListSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        places = None
        tags = self.request.data.get('tag') # Выбранные теги (что по умолчанию?)
        if self.request.user.is_authenticated:
            user = get_object_or_404(User, username=self.request.user.username)
            # tag__slug__in = tags .(distinct)
            places = Place.objects.filter(city=user.city)
        else:
            # Может вынести самый главный город(Москва) в .env??
            places = Place.objects.filter(city__name='Москва')
        return places


class PlaceView(CreateUpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    print(queryset)
    serializer_class = TagSerializer
    pagination_class = None

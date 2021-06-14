from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import pagination

from .models import Place, Tag
from .serializers import (PlaceListSerializer,
                          PlacePostSerializer,
                          TagSerializer,)
from .generics import CreateUpdateAPIView
from bbbs.common.models import User


class PlaceList(generics.ListAPIView):
    serializer_class = PlaceListSerializer
    pagination_class = pagination.PageNumberPagination
    # Добавить фильтр по тегам.

    def get_queryset(self):
        places = None
        if self.request.user.is_authenticated:
            user = get_object_or_404(User, username=self.request.user.username)
            places = Place.objects.filter(city=user.city)
        else:
            # Может вынести самый главный город(Москва) в .env??
            places = Place.objects.filter(city__name='Москва')
        return places


class PlaceView(CreateUpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacePostSerializer
    # Пока не понятно, что тут делать..


class PlaceTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None

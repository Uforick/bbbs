from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination, permissions

from .serializers import (PlaceListSerializer,
                          PlacePostSerializer,
                          TagSerializer,)
from .models import Place, Tag
from .filters import PlaceFilter
from .generics import CreateRetrieveAPIView
from bbbs.common.models import Profile

DEFAULT_CITY = 'Москва'


class PlaceListView(generics.ListAPIView):
    serializer_class = PlaceListSerializer
    pagination_class = pagination.PageNumberPagination
    filterset_class = PlaceFilter

    def get_queryset(self):
        places = None
        if self.request.user.is_authenticated:
            user = get_object_or_404(Profile, user=self.request.user)
            places = Place.objects.filter(city__name=user.user_cities[0])
        else:
            places = Place.objects.filter(city__name=DEFAULT_CITY)
        return places


class PlacePostUpdateView(CreateRetrieveAPIView):
    serializer_class = PlacePostSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        id = self.request.query_params.get('id')
        if id:
            return get_object_or_404(Place, pk=id)
        return None


class PlaceTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None

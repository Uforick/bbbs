from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from .serializers import (PlaceListSerializer,
                          PlacePostSerializer,
                          TagSerializer,)
from .models import Place, Tag
from .filters import PlaceFilter
from .generics import CreateRetrieveAPIView
from bbbs.common.models import Profile


class PlaceListView(generics.ListAPIView):
    serializer_class = PlaceListSerializer
    filterset_class = PlaceFilter

    def get_queryset(self):
        places = None
        if self.request.user.is_authenticated:
            user = get_object_or_404(Profile, user=self.request.user)
            places = Place.objects.filter(city__name=user.user_cities[0])
        else:
            city_id = self.request.query_params.get('city')
            if not city_id.isdigit():
                raise ValidationError(
                    'ID города должен быть положительным целым числом!'
                )
            places = Place.objects.filter(city__id=city_id)
        return places


class PlacePostUpdateView(CreateRetrieveAPIView):
    serializer_class = PlacePostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        id = self.request.query_params.get('id')
        if id:
            return get_object_or_404(Place, pk=id)
        return None


class PlaceTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None

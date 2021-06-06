from rest_framework import generics
from rest_framework import pagination

from .models import Place
from .serializers import PlaceSerializer


class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = pagination.PageNumberPagination


class PlaceView(generics.RetrieveUpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

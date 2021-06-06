from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from bbbs.common.models import City, Profile, Tag
from bbbs.common.serializers import (CitySerializer,
                                     ProfileSerializer, TagSerializer)


class CityList(generics.ListAPIView):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer
    pagination_class = None


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profile, user=user)


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all().order_by('-name')
    serializer_class = TagSerializer
    pagination_class = None

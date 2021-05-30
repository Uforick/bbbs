from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from bbbs.common.models import City, Profile
from bbbs.common.serializers import CitySerializer, ProfileSerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes =(IsAuthenticated,)
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profile, user=user)

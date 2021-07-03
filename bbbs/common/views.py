from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from bbbs.common.models import City, Profile
from bbbs.common.serializers import (CitySerializer, MyTokenObtainPairSerializer,
                                     ProfileSerializer)


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = None


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profile, user=user)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

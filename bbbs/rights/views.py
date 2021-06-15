from rest_framework import generics

from bbbs.rights.serializers import RightListSerializer
from bbbs.rights.models import Right


class RightList(generics.ListAPIView):
    queryset = Right.objects.all()
    serializer_class = RightListSerializer


class RightView(generics.ListAPIView):
    queryset = Right.objects.all()
    serializer_class = RightListSerializer

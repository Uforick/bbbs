from django.shortcuts import get_object_or_404
from rest_framework import filters, generics

from bbbs.rights.models import Right, RightTag
from bbbs.rights.serializers import RightSerializer, RightTagSerializer


class RightList(generics.ListAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=tag__name']


class RightView(generics.RetrieveAPIView):
    serializer_class = RightSerializer
    pagination_class = None

    def get_object(self):
        id = self.request.query_params.get('id')
        return get_object_or_404(Right, pk=id)


class RightTagList(generics.ListAPIView):
    queryset = RightTag.objects.all()
    serializer_class = RightTagSerializer
    filterset_fields = ['slug']
    pagination_class = None

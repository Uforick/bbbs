from rest_framework import generics

from bbbs.materials.models import Material
from bbbs.materials.serializers import MaterialSerializer


class MaterialListView(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

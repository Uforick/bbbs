from django_filters import FilterSet, CharFilter

from .models import Place


class PlaceFilter(FilterSet):
    search = CharFilter(field_name='tag__slug')

    class Meta:
        model = Place
        fields = ['search']

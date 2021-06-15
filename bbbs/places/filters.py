from django_filters import FilterSet, BaseCSVFilter

from .models import Place


class PlaceFilter(FilterSet):
    search = BaseCSVFilter(
        field_name='tag__slug',
        method='filter_tags'
    )

    class Meta:
        model = Place
        fields = ('search',)

    def filter_tags(self, queryset, field_name, values):
        if values:
            for value in values:
                queryset = queryset.filter(tag__slug=value)

        return queryset

import django_filters

from .models import Question


class QuestionFilter(django_filters.FilterSet):
    search = django_filters.BaseCSVFilter(
        field_name='tag__slug',
        method='filter_tags'
    )

    class Meta:
        model = Question
        fields = ('search',)

    def filter_tags(self, queryset, field_name, values):
        if values:
            for value in values:
                queryset = queryset.filter(tag__slug=value)
        return queryset

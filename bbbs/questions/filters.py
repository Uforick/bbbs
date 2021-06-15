import django_filters

from .models import Question


class QuestionFilter(django_filters.FilterSet):
    search= django_filters.BaseCSVFilter( 
        field_name = 'tag__slug',
        method='filter_tags'
    )

    class Meta:
        model = Question
        fields = ('search',)

    def filter_tags(self, queryset, field_name, values):
        # берем Question потому, что в queryset будет только "verified":true
        return Question.objects.filter(tag__slug__in=values)

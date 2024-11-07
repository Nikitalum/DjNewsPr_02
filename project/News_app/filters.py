import django_filters
from django_filters import FilterSet
from .models import Articles, Category


class ArticlesFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Articles
        fields = '__all__'
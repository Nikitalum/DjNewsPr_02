import django_filters
from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Category
from django.forms.widgets import DateTimeInput


class ArticlesFilter(FilterSet):
    name = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Название содержит')
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория'
    )
    date = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        label='Дата позднее',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        )
    )


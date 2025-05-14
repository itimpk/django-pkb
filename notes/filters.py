# notes/filters.py

import django_filters
from .models import Note
from django.db.models import Q

class NoteFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='combined_search', label='Search')

    class Meta:
        model = Note
        fields = ['q']

    def combined_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(content__icontains=value) |
            Q(tags__name__icontains=value)
        ).distinct()

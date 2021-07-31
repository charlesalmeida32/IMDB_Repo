from django_filters import FilterSet
from django_filters import filters
from .models import Movies


class MoviesFilter(FilterSet):
    '''This filter class will allow you the filter the results with any of the fields from you database'''
    name = filters.CharFilter()
    class Meta:
        model = Movies
        fields = {
            'name':['iexact', 'contains'],
            'director':['iexact', 'contains'],
            'imdb_score': ['gt', 'lt', 'exact'],
            'popularity99': ['gt', 'lt', 'exact'],
            'genre': ['contains']
        }
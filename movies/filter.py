from django_filters import FilterSet
from django_filters import filters
from .models import Movies


class MoviesFilter(FilterSet):
    '''This filter class will allow you the filter the results in your API with the below mentioned fields from you database'''
    name = filters.CharFilter()
    class Meta:
        model = Movies
        fields = {
            'name':['iexact', 'contains'],
            'director':['iexact', 'contains'],
            'imdb_score': ['gte', 'lte', 'exact'],
            'popularity99': ['gte', 'lte', 'exact'],
            'genre': ['contains']
        }
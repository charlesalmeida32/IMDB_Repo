from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.compat import md_filter_add_syntax_highlight
from .models import Movies

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.ListField()

    class Meta:
        model = Movies
        fields = "__all__"
        read_only_fields = ['created_at']




    
from django.db.models import fields
import django_filters
from .models import bookform

class BookFilter(django_filters.FilterSet):
    class meta:
        model=bookform
        fields=[
            'genre',
            'language',
        ]     
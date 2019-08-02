from django.contrib.auth.models import User
import django_filters
from .models import Assets

class AssetsFilter(django_filters.FilterSet):
    class Meta:
        model = Assets
        fields = ['asset_name']


from django.contrib.auth.models import User
import django_filters
from .models import Neighborhood, Business, Contact

class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ['contact_name', ]

class BusinessFilter(django_filters.FilterSet):
    class Meta:
        model = Business
        fields = ['business_name']

class NeighborhoodFilter(django_filters.FilterSet):
    class Meta:
        model = Neighborhood
        fields = ['neighborhood_name']
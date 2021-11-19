from django.shortcuts import render
from rest_framework import viewsets
from core.models import Geolocations

from core.serializers import GeoSerializer

# Create your views here.
class GeoViewSet(viewsets.ModelViewSet):
    queryset = Geolocations.objects.all()
    serializer_class = GeoSerializer
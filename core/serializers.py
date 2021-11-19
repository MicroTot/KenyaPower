from rest_framework import fields, serializers

from core.models import Geolocations

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocations
        fields = "__all__"
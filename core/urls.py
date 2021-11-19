from django.urls import path

from core.views import GeoViewSet

urlpatterns = [
    path('', GeoViewSet.as_view({'get': 'list'}))
]
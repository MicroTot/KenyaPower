from django.urls import path

from core.views import GeoViweSet

urlpatterns = [
    path('', GeoViweSet.as_view({'get': 'list'}))
]
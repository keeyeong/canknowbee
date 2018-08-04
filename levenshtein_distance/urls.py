from django.urls import path

from .views import LevenshteinDistanceView

urlpatterns = [
    path('', LevenshteinDistanceView.as_view(), name='index')
]

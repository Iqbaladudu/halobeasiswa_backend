from django.urls import path, include
from .views import CountriesList

urlpatterns = [
    path('countries/', CountriesList.as_view(), name='countries-list')
]

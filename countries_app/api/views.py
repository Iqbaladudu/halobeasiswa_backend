from rest_framework import generics
from .serializers import CountriesSerializer
from ..models import CountriesToStudy


class CountriesList(generics.ListAPIView):
    serializer_class = CountriesSerializer
    queryset = CountriesToStudy.objects.all()

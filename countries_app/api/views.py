from rest_framework import generics
from .serializers import CountriesSerializer
from ..models import Countries


class CountriesList(generics.ListAPIView):
    serializer_class = CountriesSerializer
    queryset = Countries.objects.all()

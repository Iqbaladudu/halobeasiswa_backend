from rest_framework import serializers
from ..models import CountriesToStudy


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountriesToStudy
        fields = '__all__'

from rest_framework import serializers
from ..models import Events


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'picture', 'date', 'time', 'status',
                  'description', 'registration_link', 'price']

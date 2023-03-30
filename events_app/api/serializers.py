from rest_framework import serializers
from ..models import Events


class EventSerializers(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, instance):
        return str(instance.description.html)

    class Meta:
        model = Events
        fields = ['name', 'picture', 'date', 'time', 'date_open', 'date_closes',
                  'status', 'description', 'registration_link', 'price', 'highlight']

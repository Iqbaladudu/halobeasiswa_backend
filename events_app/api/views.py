from rest_framework import generics
from .serializers import EventSerializers
from ..models import Events


class EventsList(generics.ListAPIView):
    serializer_class = EventSerializers
    queryset = Events

    def get_queryset(self):
        return self.queryset.objects.all()

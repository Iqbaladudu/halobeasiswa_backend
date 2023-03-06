from django.urls import path, include
from .views import EventsList

urlpatterns = [
    path('events/', EventsList.as_view(), name='events-list')
]

from django.urls import path, include
from .views import ProfileRetrieveUpdate

urlpatterns = [
    path('profile/', ProfileRetrieveUpdate.as_view(), name='edit-profile')
]

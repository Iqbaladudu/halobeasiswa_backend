from rest_framework import generics
from .serializers import ProfileSerializer
from ..models import Profile
from rest_framework import permissions


class ProfileRetrieveUpdate(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()

    def get_object(self, queryset=None):
        return self.request.user

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save()

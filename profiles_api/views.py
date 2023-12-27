from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import UpdateOwnProfile


class UserProfileViewSet(ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']

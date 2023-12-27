from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import UserProfile, UserProfileManager
from .serializers import UserProfileSerializer
from .permissions import UpdateOwnProfile

class UserProfileViewSet(ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnProfile]


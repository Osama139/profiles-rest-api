from rest_framework import serializers
from .models import UserProfile, UserProfileManager, ProfileFeedItem


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': "password"
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    """Seraializes profile feed items"""

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_at')
        extra_kwargs = {
            "user_profile": {
                "read_only": True
            }
        }

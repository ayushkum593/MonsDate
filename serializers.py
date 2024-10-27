from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import UserProfile


class UserProfileSerializer(DocumentSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):   
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}  # Password should be write-only

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

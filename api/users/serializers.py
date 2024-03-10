from rest_framework import serializers
from .models import User, Address

class UserSerializer(serializers.ModelSerializer):  
    addresses = serializers.SerializerMethodField()
    
    def get_addresses(self, user):
        if user.addresses:
            addresses = AddresSerializser(user.addresses, many = True)
            return addresses.data
        return []
     
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'avatar', 'addresses']
        extra_kwargs = {'password': {'write_only': True}}  # Password should be write-only
 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
class AddresSerializser(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__' 
        extra_kwargs = {'user': {'read_only': True}}  # Password should be write-only
        
        

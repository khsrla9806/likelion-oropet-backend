from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import User

from django.utils.translation import gettext as _

class CustomRegisterSerializer(RegisterSerializer):
    userimage = serializers.ImageField(use_url=True, allow_null=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'pk', 'userimage']
        
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['userimage'] = self.validated_data.get('userimage', '')
        return data

class CustomUserDetailSerializer(UserDetailsSerializer):
    first_name = None
    last_name = None
    
    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'userimage',]
        read_only_fields = ('email',)
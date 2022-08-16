from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from petpe.serializers import SimpleStorySerializer
from .models import User
from rest_framework.generics import ListAPIView

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

class UserFindSerializer(serializers.ModelSerializer):
    writen_story = serializers.SerializerMethodField()
    
    def get_writen_story(self, obj):
        story = obj.story_owner.all()
        serializer = SimpleStorySerializer(instance=story, many=True, read_only=True, context=self.context).data
        return serializer
    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'userimage', 'writen_story']
        read_only_fields = ('email', 'username', 'userimage')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['pk','username']
        
from rest_framework import serializers
from .models import Socialring, joinlist,SocialringComment
# from accounts.models import User


class MySocialringSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Socialring
        ordering = ['created_date']
        fields = ['id','user','image','user_jud','category','type','meetdate','meettime','maxpeople','count','flag', 'created_date']
        
class joinlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = joinlist
        fields = ['id','username','num']
        
        
class SocialringCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialringComment
        fields = ['id', 'text', 'socialring', 'created_at', 'updated_at']
        ordering = ['created_at']
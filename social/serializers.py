from rest_framework import serializers
from .models import Socialring, joinlist,SocialringComment
# from accounts.models import User


class MySocialringSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()#추가한거임 받는거
    image = serializers.ImageField(use_url=True)#원래있던거임
    
    def get_comments(self, obj):
        comment = obj.socialringcomment.all()
        return SocialringCommentSerializer(instance=comment, many=True, read_only=True, context=self.context).data
    
    class Meta:
        model = Socialring
        ordering = ['created_date']
        fields = ['id','user','title','location','image','category','type','meetdate','meettime','maxpeople','count','flag','user_jud', 'created_date','comments']
        
class joinlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = joinlist
        fields = ['id','username','num']
        
        
class SocialringCommentSerializer(serializers.ModelSerializer):
    author_username=serializers.SerializerMethodField()

    def get_author_username(self, obj):
        return obj.author.username if obj.author is not None else 'null'

    class Meta:
        model = SocialringComment
        fields = ['author_username','id', 'text', 'socialring', 'created_at', 'updated_at']
        ordering = ['created_at']
        
        
        
        
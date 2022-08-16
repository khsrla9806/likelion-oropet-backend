from rest_framework import serializers
from .models import Story, StoryComment, StroyPicture

class StoryPictureSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True) # img file의 url을 보내주기 위한 코드
    
    class Meta:
        model = StroyPicture
        fields = ['picture']

### 댓글 기능 추가 ### 2022.08.10
class CommentSerializer(serializers.ModelSerializer):
    author_useremail = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()
    author_userimage = serializers.SerializerMethodField()
    
    def get_author_username(self, obj):
        return obj.author.username if obj.author is not None else 'null'
    def get_author_useremail(self, obj):
        return obj.author.email if obj.author is not None else 'null'
    def get_author_userimage(self, obj):
        request = self.context.get('request')
        if obj.author.userimage:
            return request.build_absolute_uri(obj.author.userimage.url)
        else:
            return 'null'
    
    class Meta:
        model = StoryComment
        fields = ['id', 'text', 'story', 'author_id', 'author_useremail', 'author_username', 'author_userimage', 'createdAt', 'updatedAt']
        ordering = ['-createdAt']

class StorySerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField() # Story에는 없는 필드를 형성하기 위한 코드
    username = serializers.SerializerMethodField()
    useremail = serializers.SerializerMethodField()
    userimage = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    
    def get_pictures(self, obj):
        picture = obj.storypicture.all() # related_name 으로 picture을 역참조 해서 queryset으로 반환
        return StoryPictureSerializer(instance=picture, many=True, context=self.context).data # context=self.context를 상대경로가 아닌 전체 url이 나온다. 
    def get_username(self, obj):
        return obj.user.username if obj.user is not None else 'null'
    def get_useremail(self, obj):
        return obj.user.email if obj.user is not None else 'null'
    def get_userimage(self, obj):
        request = self.context.get('request')
        if obj.user.userimage:
            return request.build_absolute_uri(obj.user.userimage.url)
        else:
            return 'null'
    def get_comments(self, obj):
        comment = obj.storycomment.all()
        return CommentSerializer(instance=comment, many=True, read_only=True, context=self.context).data
    
    class Meta:
        model = Story
        fields = ['id', 'title', 'content', 'pictures', 'createdAt', 'updatedAt', 'user_id', 'username', 'useremail', 'userimage', 'comments', 'image_likes']
        read_only_fields = ['image_likes']
    
    def create(self, validated_data):
        instance = Story.objects.create(**validated_data)
        storypicture_set = self.context['request'].FILES
        for pic_data in storypicture_set.getlist('picture'):
            StroyPicture.objects.create(story=instance, picture=pic_data)
        return instance

class SimpleStorySerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField()
    def get_pictures(self, obj):
        picture = obj.storypicture.all() 
        return StoryPictureSerializer(instance=picture, many=True, context=self.context).data # context=self.context를 상대경로가 아닌 전체 url이 나온다.
    class Meta:
        model = Story
        fields = ['id', 'pictures', 'createdAt', 'updatedAt']
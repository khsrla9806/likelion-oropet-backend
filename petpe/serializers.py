from rest_framework import serializers
from .models import MyStory, Story, StroyPicture

class MyStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyStory
        fields = '__all__'
        
class StoryPictureSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True) # img file의 url을 보내주기 위한 코드
    
    class Meta:
        model = StroyPicture
        fields = ['picture']

class StorySerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField() # Story에는 없는 필드를 형성하기 위한 코드
    
    def get_pictures(self, obj):
        picture = obj.picture.all() # related_name 으로 picture을 역참조 해서 queryset으로 반환
        return StoryPictureSerializer(instance=picture, many=True, context=self.context).data # context=self.context를 상대경로가 아닌 전체 url이 나온다. 
    
    class Meta:
        model = Story
        fields = '__all__'
    
    def create(self, validated_data):
        instance = Story.objects.create(**validated_data)
        storypicture_set = self.context['request'].FILES
        for pic_data in storypicture_set.getlist('picture'):
            StroyPicture.objects.create(story=instance, picture=pic_data)
        return instance
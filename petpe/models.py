from django.db import models
# from django.contrib.auth.models import User

# 이미지 1개 업로드 가능
class MyStory(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='pictures/')
    
    def __str__(self):
        return self.title
    
# 이미지 여러개 업로드 가능한 기능 찾기
class Story(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'story'

class StroyPicture(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='picture')
    picture = models.ImageField(default=None, null=True, upload_to='storypictures/')
    
    class Meta:
        db_table = 'story_picture'
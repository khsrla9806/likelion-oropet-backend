from django.db import models
from accounts.models import User

class Socialring(models.Model):
    
    opt1= "workout"
    opt2= "food"
    opt3= "travel"
    opt4= "education"
    opt5= "growth"
    CHOICES = ((opt1, "workout"), (opt2, "food"),(opt3, "travel"), (opt4, "education"),(opt5, "growth"))
    category = models.CharField(
        choices=CHOICES, max_length=50, null=True, blank=True
    )
    
    on= "online"
    off= "offline"
    ONOFF = ((on, "online"), (off,"offline"))
    type = models.CharField(
        choices=ONOFF, max_length=50, null=True, blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #id값으로 받아짐, 화면 노출X(getX), Post 요청만
    image = models.ImageField(
        default=None, null=True, blank=True)
    meetdate = models.DateField(null=True)
    meettime = models.TimeField(null=True)
    maxpeople = models.IntegerField(null=True)
    count=models.IntegerField(default=0,blank=True) #값 받기X->화면에 표시만...
    created_date = models.DateTimeField(auto_now_add=True) #값 받기X->화면에 표시만...
    flag=models.CharField(max_length=50,null=True,blank=True) #값 받기X->화면에 표시만...
    user_jud=models.CharField(max_length=50,null=True, blank=True) #로그인 판단(로그인이 확인되면 True->counting URL연결, 아니면 False 로그인 하라는 멘트)
    title=models.CharField(max_length=50, null=True) #소셜링 제목
    location=models.CharField(max_length=50,null=True) #위치


class joinlist(models.Model):   
    num = models.ForeignKey(Socialring, on_delete=models.CASCADE, null=True) #id값으로 받아짐, 화면 노출X(getX), Post 요청만
    username = models.CharField(max_length=30, unique=True, null=True)


class SocialringComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    socialring = models.ForeignKey(Socialring, on_delete=models.CASCADE,related_name='socialringcomment')
    comment_id=models.IntegerField(null=True,blank=True)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.text
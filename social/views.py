from gc import get_objects
from itertools import count
from os import DirEntry
from re import A
from xml.dom.xmlbuilder import DOMEntityResolver
from django.shortcuts import render, redirect
from rest_framework import viewsets

import social
from .models import Socialring, joinlist,SocialringComment
from .serializers import MySocialringSerializer,joinlistSerializer,SocialringCommentSerializer
from accounts.models import User #USER 받아오기
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .forms import JoinForm
from social import serializers



class MySocialringViewSet(viewsets.ModelViewSet):
    queryset = Socialring.objects.all().order_by('-created_date')
    serializer_class = MySocialringSerializer
          

class JoinViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=joinlist.objects.all()
        serializer=joinlistSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        queryset = joinlist.objects.filter(num=pk)
        serializer=joinlistSerializer(queryset, many=True)
        return Response(serializer.data)





def join(request,pk):
    if request.method == "POST":
        social=Socialring.objects.get(id=pk)
        if request.user.is_authenticated:  #사용자가 로그인 한 경우 True 반환
            social.user_jud='True' #로그인 확인 완료
            if social.count<=social.maxpeople:  
                    social.count=social.count+1
                    social.flag='True' #참가허가 O
                    # if social.count<social.maxpeople:
                    #     social.flag='False' #참가허가 x
                    social.save() #db save 실제 카운팅
                    Form=JoinForm(request.POST)
                    if Form.is_valid():
                        finish_form=Form.save(commit=False)
                        finish_form.num=get_object_or_404(Socialring,pk=pk)
                        finish_form.save()
            else:   #참가허가X
                social.flag='False'
                social.save() #db save 실제 카운팅


# def join_save(request,pk):   #pk:방번호 정보 저장하기, 정보 뽑기
#     Form=JoinForm(request.POST)
#     if Form.is_valid():
#         finish_form=Form.save(commit=False)
#         finish_form.num=get_object_or_404(Socialring,pk=pk)
#         finish_form.save()
        

class CommentViewSet(viewsets.ModelViewSet):
    queryset = SocialringComment.objects.all()
    serializer_class = SocialringCommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
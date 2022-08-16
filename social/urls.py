from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from.views import JoinViewSet,CommentViewSet

router = routers.DefaultRouter()


router.register('socialring', views.MySocialringViewSet), #방 만들기
router.register('joinlist', views.JoinViewSet, basename='view') #참여자 리스트, pk 값=방번호 ex)joinlist/1->1번방 참여 회원 리스트
router.register(r'comments', views.CommentViewSet)

view_list=JoinViewSet.as_view({'get':'list'})
view_detail=JoinViewSet.as_view({'get':'retrieve'})
urlpatterns = [
    path('', include(router.urls)),
    path('socialring/<int:pk>/join',views.join, name='join'), #참여 확인 함수 및 참가 회원 저장 함수
    # path('socialring/<int:pk>/save',views.join_save, name='save'), #참가한 회원 db 저장함수 **실험용
    

] 
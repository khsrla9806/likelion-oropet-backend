from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
# 사진등록을 위한 url 설정
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('mystory', views.MyStoryViewSet)
router.register('story', views.StoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
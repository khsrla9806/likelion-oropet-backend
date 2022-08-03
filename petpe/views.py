from django.shortcuts import render
from rest_framework import viewsets
from .models import MyStory, Story
from .serializers import MyStorySerializer, StorySerializer

class MyStoryViewSet(viewsets.ModelViewSet):
    queryset = MyStory.objects.all().order_by('-createdAt')
    serializer_class = MyStorySerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
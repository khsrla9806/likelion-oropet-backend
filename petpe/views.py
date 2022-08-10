from django.shortcuts import render
from rest_framework import viewsets
from .models import Story, StoryComment
from .serializers import CommentSerializer, StorySerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_update(serializer)

### 댓글 기능 추가 ### 2022.08.10
class CommentViewSet(viewsets.ModelViewSet):
    queryset = StoryComment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
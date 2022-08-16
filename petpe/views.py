from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Story, StoryComment
from .serializers import CommentSerializer, StorySerializer

from django.views.decorators.http import require_POST
from django.http import HttpResponse
from accounts.models import User
from rest_framework.pagination import LimitOffsetPagination

class StoryPagination(LimitOffsetPagination):
    default_limit=10

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    pagination_class=StoryPagination
    
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

@require_POST
def story_likeview(request, story_id):
    if request.user.is_authenticated:
        story = get_object_or_404(Story, pk=story_id)
        
        if story.image_likes.filter(email=request.user.email).exists():
            story.image_likes.remove(User.objects.get(email=request.user.email))
            return HttpResponse(content = "좋아요 취소")
        else:
            story.image_likes.add(User.objects.get(email=request.user.email))
            return HttpResponse(content = "좋아요")
    return HttpResponse(status=400)
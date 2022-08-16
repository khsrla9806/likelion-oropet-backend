from django.shortcuts import render
from accounts.models import User
from rest_framework.generics import ListAPIView
from accounts.serializers import UserSerializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

class UserSearchPagination(LimitOffsetPagination):
    default_limit=4
class UserListView(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    pagination_class=UserSearchPagination
    filter_backends=[SearchFilter]
    search_fields=['username']

    
# Create your views here.

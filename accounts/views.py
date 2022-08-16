from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserFindSerializer
from .models import User

class UserFindView(RetrieveUpdateAPIView):
    serializer_class = UserFindSerializer
    lookup_url_kwarg = 'user_id'
    queryset = User.objects.all()

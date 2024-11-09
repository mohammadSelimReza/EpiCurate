from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import UserInfo
from django.contrib.auth.models import User
from .serializers import UserSerializers, UserCreationSerializer
from rest_framework import generics
import django_filters.rest_framework


# Create your views here.
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class UserCreationView(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserCreationSerializer

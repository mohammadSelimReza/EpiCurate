from django.shortcuts import render
from . import serializers
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import UserBioData, User


# Create your views here.
class UserCreationView(viewsets.ModelViewSet):
    queryset = UserBioData.objects.all()
    serializer_class = serializers.UserCreationSerializer

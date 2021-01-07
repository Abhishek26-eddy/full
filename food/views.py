from django.shortcuts import render

# Create your views here.

from .models import Profile, Skills
from .serializers import ProfileSerializer, SkillSerializer
from rest_framework import generics
from .validators import is_present

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class SkillList(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer


class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer

    
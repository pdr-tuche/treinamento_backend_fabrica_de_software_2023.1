from django.shortcuts import render
from rest_framework import viewsets
from .models import Anime
from .serializers import AnimeSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
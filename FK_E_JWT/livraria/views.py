from django.shortcuts import render
from rest_framework import viewsets
from .models import Livraria
from .serializer import LivrariaSerializer
class LivrariaViewSet(viewsets.ModelViewSet):
    queryset = Livraria.objects.all()
    serializer_class = LivrariaSerializer

# Create your views here.

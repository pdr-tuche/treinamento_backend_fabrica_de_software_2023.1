from django.shortcuts import render
from rest_framework import viewsets
from .models import Livro
from .serializer import LivroSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class LivroViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = [TokenAuthentication]

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# Create your views here.

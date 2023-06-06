from django.db import models
from livro.models import Livro

class Livraria(models.Model):
    nome = models.CharField(max_length=123)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome}'
from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=123)

    def __str__(self):
        return f'{self.titulo}'
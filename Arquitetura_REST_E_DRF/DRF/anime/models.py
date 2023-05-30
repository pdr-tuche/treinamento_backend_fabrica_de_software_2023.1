from django.db import models

class Anime(models.Model):
    titulo = models.CharField(max_length=120)
    genero = models.CharField(max_length=120)


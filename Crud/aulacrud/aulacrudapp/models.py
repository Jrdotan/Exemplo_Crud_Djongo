from django.db import models

# Create your models here.

class posts(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()


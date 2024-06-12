from django.db import models

# Create your models here.

class Itens(models.Model):
    name = models.CharField(max_length=240)
    descript = models.TextField()
    path = models.ImageField(upload_to="imagens/")
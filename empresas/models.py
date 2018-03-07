from django.db import models

class Empresas(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

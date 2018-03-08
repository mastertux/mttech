from django.db import models

class Empresas(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    ramo_atividade = models.CharField(
        max_length=100,
        null=False,
        blank=True
    )

    class Meta:
        db_table = 'empresas'
        managed = True
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
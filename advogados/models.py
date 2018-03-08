from django.db import models

from django.db import models

class Advogados(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=13,
        null=False,
        blank=False
    )
    
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False,
        unique=True
    )

    cpf = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        unique=True
    )

    class Meta:
        db_table = 'advogados'
        managed = True
        verbose_name = 'Advogado'
        verbose_name_plural = 'Advogados'

    def __str__(self):
        return self.nome

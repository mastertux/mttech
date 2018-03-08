from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_advogado = models.BooleanField('advogado status', default=False)
    is_empresa = models.BooleanField('empresa status', default=False)
    empresa = models.ForeignKey('empresas.Empresas', on_delete=models.CASCADE, null=True, blank=True)
    advogado = models.ForeignKey('advogados.Advogados', on_delete=models.CASCADE, null=True, blank=True)

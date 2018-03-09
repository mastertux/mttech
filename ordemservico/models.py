from django.db import models


class OrdemServico(models.Model):
    STATUS_ORDEM_SERVICO = (
        (1, 'Criada'),
        (2, 'Delegada'),
        (3, 'Finalizada'),
    )

    titulo = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    empresa = models.ForeignKey(
        'empresas.Empresas',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    descricao = models.TextField(
        null=False,
        blank=False
    )

    status = models.PositiveSmallIntegerField(
        choices=STATUS_ORDEM_SERVICO, 
        default=1, 
        blank=True
    )

    class Meta:
        db_table = 'ordem_servicos'
        managed = True
        verbose_name = 'Ordem Serviço'
        verbose_name_plural = 'Ordens de Serviços'
    
        


class Proposta(models.Model):
    STATUS_PROPOSTA = (
        (1, 'Aberta'),
        (2, 'Aceita'),
        (3, 'Recusada'),
    )
    
    ordem_servico = models.ForeignKey(
        'OrdemServico',
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )
    
    advogado = models.ForeignKey(
        'advogados.Advogados',
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )
    
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.PositiveSmallIntegerField(
        choices=STATUS_PROPOSTA, 
        default=1, 
        blank=True
    )
    class Meta:
        db_table = 'propostas'
        managed = True
        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'
        unique_together = (('advogado', 'ordem_servico'),)
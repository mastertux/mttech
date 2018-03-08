# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-08 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advogados', '0001_initial'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Criada'), (2, 'Delegada'), (3, 'Finalizada')])),
                ('empresa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresas')),
            ],
            options={
                'verbose_name': 'Ordem Serviço',
                'verbose_name_plural': 'Ordens de Serviços',
                'db_table': 'ordem_servicos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advogado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advogados.Advogados')),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordemservico.OrdemServico')),
            ],
            options={
                'verbose_name': 'Proposta',
                'verbose_name_plural': 'Propostas',
                'db_table': 'propostas',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='proposta',
            unique_together=set([('advogado', 'ordem_servico')]),
        ),
    ]

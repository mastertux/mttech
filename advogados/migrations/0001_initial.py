# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-07 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advogados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
            ],
            options={
                'verbose_name': 'Advogado',
                'verbose_name_plural': 'Advogados',
                'db_table': 'advogados',
                'managed': True,
            },
        ),
    ]
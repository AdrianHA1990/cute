# Generated by Django 4.2.2 on 2023-07-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cute_paginas', '0002_alter_clientes_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=100, verbose_name='Telefono'),
        ),
    ]

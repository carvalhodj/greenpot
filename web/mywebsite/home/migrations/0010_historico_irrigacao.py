# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_planta_umidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico_irrigacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_do_acionamento', models.CharField(max_length=10)),
                ('umidade_inicio', models.CharField(max_length=10)),
                ('pote', models.ForeignKey(to='home.Pote')),
            ],
        ),
    ]

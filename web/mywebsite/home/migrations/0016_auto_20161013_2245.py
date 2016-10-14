# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20161013_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_irrigacao',
            name='hora_do_desligamento',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='historico_irrigacao',
            name='umidade_final',
            field=models.CharField(max_length=10),
        ),
    ]

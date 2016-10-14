# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20161013_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_irrigacao',
            name='hora_do_desligamento',
            field=models.CharField(default=b'0000000', max_length=10),
        ),
        migrations.AlterField(
            model_name='historico_irrigacao',
            name='umidade_final',
            field=models.CharField(default=b'0000000', max_length=10),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_pote_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='descricao_planta',
            field=models.CharField(max_length=1500),
        ),
    ]

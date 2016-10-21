# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_historico_irrigacao_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='pote',
            name='regiao',
            field=models.CharField(default='ibura', max_length=10),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_pote_regiao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_irrigacao',
            name='data',
            field=models.DateTimeField(default=datetime.date(2016, 10, 20), editable=False),
        ),
    ]

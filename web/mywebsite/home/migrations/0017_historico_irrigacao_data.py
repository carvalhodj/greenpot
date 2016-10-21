# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20161013_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='historico_irrigacao',
            name='data',
            field=models.DateTimeField(default=datetime.date(2016, 10, 19), editable=False),
        ),
    ]

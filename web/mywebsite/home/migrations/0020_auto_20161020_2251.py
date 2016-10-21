# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20161020_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_irrigacao',
            name='data',
            field=models.DateField(default=datetime.date(2016, 10, 20), editable=False),
        ),
    ]

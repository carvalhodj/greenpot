# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20160930_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='umidade',
            field=models.CharField(default=datetime.datetime(2016, 10, 4, 19, 17, 13, 477467, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]

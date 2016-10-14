# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_pote_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='historico_irrigacao',
            name='hora_do_desligamento',
            field=models.CharField(default=datetime.datetime(2016, 10, 14, 0, 53, 44, 376000, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historico_irrigacao',
            name='umidade_final',
            field=models.CharField(default=datetime.datetime(2016, 10, 14, 0, 53, 57, 912000, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]

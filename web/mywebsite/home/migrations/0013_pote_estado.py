# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20161009_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='pote',
            name='estado',
            field=models.BooleanField(default=1),
        ),
    ]

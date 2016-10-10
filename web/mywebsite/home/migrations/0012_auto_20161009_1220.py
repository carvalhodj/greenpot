# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20161008_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pote',
            name='codigo',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]

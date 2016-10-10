# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_historico_irrigacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pote',
            name='id',
        ),
        migrations.AlterField(
            model_name='pote',
            name='codigo',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]

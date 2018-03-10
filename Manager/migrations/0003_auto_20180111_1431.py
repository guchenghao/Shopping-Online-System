# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_auto_20180111_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='detail',
        ),
        migrations.AlterField(
            model_name='products',
            name='info',
            field=models.CharField(max_length=1000),
        ),
    ]

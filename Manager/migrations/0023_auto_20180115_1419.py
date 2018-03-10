# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0022_auto_20180115_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='produceTime',
            field=models.DateField(null=True),
        ),
    ]

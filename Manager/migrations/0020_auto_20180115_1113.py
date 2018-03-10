# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0019_auto_20180115_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='productType',
            field=models.CharField(max_length=100),
        ),
    ]

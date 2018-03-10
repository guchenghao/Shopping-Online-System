# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0013_auto_20180115_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='expTime',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]

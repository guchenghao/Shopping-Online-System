# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0008_auto_20180113_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='expTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='produceTime',
            field=models.DateField(null=True),
        ),
    ]

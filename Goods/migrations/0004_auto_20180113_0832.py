# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0003_auto_20180112_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='productName',
            field=models.CharField(max_length=500),
        ),
    ]

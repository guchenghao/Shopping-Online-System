# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0006_remove_orderlist_ordertime'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='orderTime',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]

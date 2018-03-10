# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0005_auto_20180115_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlist',
            name='orderTime',
        ),
    ]

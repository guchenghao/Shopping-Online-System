# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0015_auto_20180115_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='produceTime',
        ),
    ]

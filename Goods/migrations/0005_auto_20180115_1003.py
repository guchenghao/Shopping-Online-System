# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0004_auto_20180113_0832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderlist',
            options={'ordering': ['-id']},
        ),
    ]

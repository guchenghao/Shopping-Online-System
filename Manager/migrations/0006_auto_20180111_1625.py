# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0005_auto_20180111_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='type',
            new_name='productType',
        ),
    ]

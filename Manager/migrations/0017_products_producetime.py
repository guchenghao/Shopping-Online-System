# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0016_remove_products_producetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='produceTime',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]

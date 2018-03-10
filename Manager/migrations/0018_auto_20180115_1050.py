# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0017_products_producetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='produceTime',
        ),
        migrations.RemoveField(
            model_name='products',
            name='saleTime',
        ),
    ]

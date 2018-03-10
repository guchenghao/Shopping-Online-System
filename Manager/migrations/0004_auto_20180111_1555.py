# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_auto_20180111_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(upload_to=b'goods_image'),
        ),
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]

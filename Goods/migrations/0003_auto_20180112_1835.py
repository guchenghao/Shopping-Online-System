# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_orderdetail_orderlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='pic_url',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='productName',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='username',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]

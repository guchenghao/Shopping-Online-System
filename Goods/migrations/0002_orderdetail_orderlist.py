# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderID', models.IntegerField()),
                ('productID', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('buyPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='orderList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cusID', models.IntegerField()),
                ('orderTime', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('totalPrice', models.FloatField()),
                ('orderState', models.CharField(max_length=30)),
            ],
        ),
    ]

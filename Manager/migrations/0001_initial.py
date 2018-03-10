# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id',
                 models.AutoField(
                     verbose_name='ID',
                     serialize=False,
                     auto_created=True,
                     primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('productType', models.CharField(max_length=10)),
                ('produceTime', models.DateField()),
                ('picture', models.ImageField(upload_to=b'')),
                ('expTime', models.IntegerField()),
                ('price', models.FloatField()),
                ('info', models.CharField(max_length=1000)),
                ('saleTime', models.DateField()),
                ('Inventory', models.IntegerField()),
            ],
        ),
    ]

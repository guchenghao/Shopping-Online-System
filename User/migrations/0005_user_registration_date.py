# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_remove_user_registration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registration_date',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]

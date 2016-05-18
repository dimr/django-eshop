# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20150531_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='main',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productimage',
            name='name',
            field=models.CharField(default=b'18e88aff', max_length=50),
        ),
    ]

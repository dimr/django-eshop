# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20150802_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='address',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='country',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]

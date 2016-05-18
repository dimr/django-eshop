# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clients.models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20150802_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='the_id',
            field=models.CharField(default=clients.models.gen_uuid, unique=True, max_length=30),
        ),
    ]

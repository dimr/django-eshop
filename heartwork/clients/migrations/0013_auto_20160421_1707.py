# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import clients.models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_auto_20160421_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='profile_url',
            field=models.CharField(default=clients.models.gen_uuid, max_length=255),
        ),
    ]

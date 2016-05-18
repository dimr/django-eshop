# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20150803_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientprofile',
            old_name='the_id',
            new_name='profile_url',
        ),
    ]

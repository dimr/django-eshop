# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_auto_20160421_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=65, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=70, blank=True),
        ),
    ]

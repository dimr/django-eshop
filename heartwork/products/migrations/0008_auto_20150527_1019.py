# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150526_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['updated']},
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_name',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150527_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image_name',
        ),
    ]

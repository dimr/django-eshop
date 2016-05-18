# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20150605_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='name',
            field=models.CharField(default=products.models.gen_uuid, max_length=50),
        ),
    ]

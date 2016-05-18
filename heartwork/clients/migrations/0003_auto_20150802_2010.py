# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_clientprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='the_client',
            field=models.OneToOneField(related_name='client', to=settings.AUTH_USER_MODEL),
        ),
    ]

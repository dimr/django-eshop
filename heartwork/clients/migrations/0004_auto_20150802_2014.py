# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20150802_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='the_client',
            field=models.OneToOneField(related_name='client_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]

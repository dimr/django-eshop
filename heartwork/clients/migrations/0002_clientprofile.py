# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clients.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('the_id', models.CharField(default=clients.models.gen_uuid, max_length=30)),
                ('address', models.CharField(max_length=30, blank=True)),
                ('country', models.CharField(max_length=30)),
                ('the_client', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

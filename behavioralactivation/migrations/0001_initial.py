# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSchedule',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('sleeping', models.IntegerField(default=0)),
                ('mastery', models.IntegerField(default=0)),
                ('pleasure', models.IntegerField(default=0)),
                ('rumination', models.IntegerField(default=0)),
                ('distractionAndAvoidance', models.IntegerField(default=0)),
                ('miscellaneous', models.IntegerField(default=0)),
                ('submit_date', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cbt2', '0008_auto_20150702_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeliefsEventsNats',
            fields=[
                ('BeliefsEventsNatsID', models.IntegerField(serialize=False, primary_key=True)),
                ('BeliefsEventsNats_text', models.TextField()),
                ('category', models.CharField(blank=True, null=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserBeliefsEventsNats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('beliefs_events_nats', models.ForeignKey(to='cbt2.BeliefsEventsNats')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userbeliefseventsnats',
            unique_together=set([('user', 'beliefs_events_nats')]),
        ),
    ]

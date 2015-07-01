# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbt2', '0006_auto_20150620_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='asweek6',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='asweek7',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='dsasweek6',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='dsasweek7',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]

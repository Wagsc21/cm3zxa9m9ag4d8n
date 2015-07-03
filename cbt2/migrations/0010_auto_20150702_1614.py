# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbt2', '0009_auto_20150702_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beliefseventsnats',
            name='category',
            field=models.CharField(choices=[('corebelief', 'Corebelief'), ('intermediatebelief', 'Intermediatebelief'), ('persistentnat', 'PersistentNAT'), ('event', 'Event')], max_length=25, default='event'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0013_shownlisttouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shownlisttouser',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='shownlisttouser',
            unique_together=set([('user', 'technique')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0011_defaultconversation'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='technique',
            unique_together=set([('module_number', 'technique_text')]),
        ),
    ]

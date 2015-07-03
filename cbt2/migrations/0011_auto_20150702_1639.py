# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbt2', '0010_auto_20150702_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beliefseventsnats',
            old_name='BeliefsEventsNatsID',
            new_name='beliefseventsnatsID',
        ),
        migrations.RenameField(
            model_name='beliefseventsnats',
            old_name='BeliefsEventsNats_text',
            new_name='beliefseventsnats_text',
        ),
    ]

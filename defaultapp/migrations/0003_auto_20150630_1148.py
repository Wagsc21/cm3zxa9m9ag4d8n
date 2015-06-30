# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0002_auto_20150629_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaultconversation',
            old_name='conversation',
            new_name='conversationID',
        ),
    ]

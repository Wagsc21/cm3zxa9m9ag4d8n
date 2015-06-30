# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0012_auto_20150629_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userconversation',
            old_name='conversation',
            new_name='dialog',
        ),
    ]

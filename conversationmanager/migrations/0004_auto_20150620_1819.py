# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0003_auto_20150620_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversations',
            old_name='conversation_text',
            new_name='dialog_text',
        ),
    ]

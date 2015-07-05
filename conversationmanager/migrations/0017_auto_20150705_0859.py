# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0016_remove_dialogs_user_conversation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userconversation',
            name='conversationID',
        ),
        migrations.RemoveField(
            model_name='userconversation',
            name='dialog',
        ),
        migrations.RemoveField(
            model_name='userconversation',
            name='option_selected',
        ),
        migrations.RemoveField(
            model_name='userconversation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Userconversation',
        ),
    ]

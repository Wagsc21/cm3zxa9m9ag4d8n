# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0010_auto_20150629_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationoptiongraph',
            name='current_dialog',
        ),
        migrations.RemoveField(
            model_name='conversationoptiongraph',
            name='next_dialog',
        ),
        migrations.RemoveField(
            model_name='conversationoptiongraph',
            name='option',
        ),
        migrations.RemoveField(
            model_name='dialogs',
            name='conversationID',
        ),
        migrations.RemoveField(
            model_name='dialogs',
            name='option',
        ),
        migrations.RemoveField(
            model_name='dialogs',
            name='user_conversation',
        ),
        migrations.RemoveField(
            model_name='userconversation',
            name='conversation',
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
            name='Conversationoptiongraph',
        ),
        migrations.DeleteModel(
            name='Dialogs',
        ),
        migrations.DeleteModel(
            name='Options',
        ),
        migrations.DeleteModel(
            name='Userconversation',
        ),
    ]

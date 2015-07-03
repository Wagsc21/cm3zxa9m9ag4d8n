# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20150630_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationtoconversation',
            name='base_conversation',
        ),
        migrations.RemoveField(
            model_name='conversationtoconversation',
            name='technique_conversation',
        ),
        migrations.RemoveField(
            model_name='conversationtomodule',
            name='conversationID',
        ),
        migrations.DeleteModel(
            name='ConversationToConversation',
        ),
        migrations.DeleteModel(
            name='ConversationToModule',
        ),
        migrations.DeleteModel(
            name='ExerciseConversation',
        ),
    ]

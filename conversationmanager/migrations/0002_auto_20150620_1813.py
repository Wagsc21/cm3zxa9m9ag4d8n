# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationoption',
            name='crrent_conversation',
        ),
        migrations.RemoveField(
            model_name='conversationoption',
            name='next_converssation',
        ),
        migrations.RemoveField(
            model_name='conversationoption',
            name='option',
        ),
        migrations.RemoveField(
            model_name='conversations',
            name='option',
        ),
        migrations.RemoveField(
            model_name='conversations',
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
            name='Conversationoption',
        ),
        migrations.DeleteModel(
            name='Conversations',
        ),
        migrations.DeleteModel(
            name='Options',
        ),
        migrations.DeleteModel(
            name='Userconversation',
        ),
    ]

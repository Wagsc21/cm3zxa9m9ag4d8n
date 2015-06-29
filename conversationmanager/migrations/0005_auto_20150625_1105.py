# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0004_auto_20150620_1819'),
    ]

    operations = [
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
        migrations.AlterModelOptions(
            name='conversations',
            options={'ordering': ['dialog']},
        ),
        migrations.RemoveField(
            model_name='conversations',
            name='user_conversation',
        ),
        migrations.AlterField(
            model_name='conversations',
            name='dialog',
            field=models.IntegerField(verbose_name='dialog ID', serialize=False, primary_key=True),
        ),
        migrations.DeleteModel(
            name='Userconversation',
        ),
    ]

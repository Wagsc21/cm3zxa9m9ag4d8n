# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0006_auto_20150625_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userconversation',
            options={'ordering': ['-conversation_time', 'user']},
        ),
        migrations.AddField(
            model_name='userconversation',
            name='conversationID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

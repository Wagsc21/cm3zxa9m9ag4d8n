# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0006_auto_20150630_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corebeliefconversation',
            name='conversationID',
        ),
        migrations.RemoveField(
            model_name='corebeliefconversation',
            name='corebelief',
        ),
        migrations.RemoveField(
            model_name='defaultconversation',
            name='conversationID',
        ),
        migrations.RemoveField(
            model_name='eventlistconversation',
            name='conversationID',
        ),
        migrations.RemoveField(
            model_name='eventlistconversation',
            name='eventlist',
        ),
        migrations.RemoveField(
            model_name='intermediatebeliefconversation',
            name='conversationID',
        ),
        migrations.RemoveField(
            model_name='intermediatebeliefconversation',
            name='intermediatebelief',
        ),
        migrations.RemoveField(
            model_name='persistentnatconversation',
            name='conversationID',
        ),
        migrations.RemoveField(
            model_name='persistentnatconversation',
            name='persistentnat',
        ),
        migrations.DeleteModel(
            name='CorebeliefConversation',
        ),
        migrations.DeleteModel(
            name='DefaultConversation',
        ),
        migrations.DeleteModel(
            name='EventlistConversation',
        ),
        migrations.DeleteModel(
            name='IntermediatebeliefConversation',
        ),
        migrations.DeleteModel(
            name='PersistentnatConversation',
        ),
    ]

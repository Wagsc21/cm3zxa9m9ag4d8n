# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseConversation',
            fields=[
                ('conversationID', models.IntegerField(primary_key=True, serialize=False)),
                ('conversation_text', models.TextField()),
            ],
        ),
    ]

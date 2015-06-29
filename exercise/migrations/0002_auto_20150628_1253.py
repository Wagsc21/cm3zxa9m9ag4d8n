# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exerciseconversation',
            options={'ordering': ['conversationID']},
        ),
        migrations.AddField(
            model_name='exerciseconversation',
            name='conversation_type',
            field=models.CharField(default='Base', max_length=255),
        ),
    ]

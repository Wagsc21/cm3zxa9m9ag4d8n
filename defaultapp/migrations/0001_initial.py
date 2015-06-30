# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0008_conversation'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultConversation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('module_number', models.IntegerField()),
                ('technique', models.CharField(max_length=255, null=True)),
                ('conversation', models.ForeignKey(to='conversationmanager.Conversation')),
            ],
        ),
    ]

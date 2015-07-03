# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0015_conversationhistory'),
        ('defaultapp', '0010_auto_20150702_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('technique', models.ForeignKey(to='defaultapp.Technique')),
            ],
            options={
                'ordering': ['technique'],
            },
        ),
    ]

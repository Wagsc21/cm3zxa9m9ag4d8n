# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0014_auto_20150630_1148'),
        ('cbt2', '0006_auto_20150620_1239'),
        ('defaultapp', '0003_auto_20150630_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntermediatebeliefConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('module_number', models.IntegerField()),
                ('technique', models.CharField(max_length=255, null=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('intermediatebelief', models.ForeignKey(to='cbt2.Intermediatebelief')),
            ],
        ),
    ]

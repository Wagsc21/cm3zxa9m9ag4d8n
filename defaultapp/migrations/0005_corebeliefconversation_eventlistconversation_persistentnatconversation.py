# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0014_auto_20150630_1148'),
        ('cbt2', '0006_auto_20150620_1239'),
        ('defaultapp', '0004_intermediatebeliefconversation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorebeliefConversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('module_number', models.IntegerField()),
                ('technique', models.CharField(max_length=255, null=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('intermediatebelief', models.ForeignKey(to='cbt2.Corebelief')),
            ],
        ),
        migrations.CreateModel(
            name='EventlistConversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('module_number', models.IntegerField()),
                ('technique', models.CharField(max_length=255, null=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('intermediatebelief', models.ForeignKey(to='cbt2.Eventlist')),
            ],
        ),
        migrations.CreateModel(
            name='PersistentnatConversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('module_number', models.IntegerField()),
                ('technique', models.CharField(max_length=255, null=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('intermediatebelief', models.ForeignKey(to='cbt2.Persistentnat')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversationmanager', '0015_conversationhistory'),
        ('cbt2', '0007_auto_20150701_1202'),
        ('defaultapp', '0007_auto_20150701_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorebeliefConversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('corebelief', models.ForeignKey(to='cbt2.Corebelief')),
            ],
        ),
        migrations.CreateModel(
            name='DefaultConversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
            ],
            options={
                'ordering': ['technique'],
            },
        ),
        migrations.CreateModel(
            name='EventlistConversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('eventlist', models.ForeignKey(to='cbt2.Eventlist')),
            ],
        ),
        migrations.CreateModel(
            name='IntermediatebeliefConversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('intermediatebelief', models.ForeignKey(to='cbt2.Intermediatebelief')),
            ],
        ),
        migrations.CreateModel(
            name='PersistentnatConversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('persistentnat', models.ForeignKey(to='cbt2.Persistentnat')),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('technique_id', models.IntegerField(serialize=False, primary_key=True)),
                ('module_number', models.IntegerField()),
                ('technique_text', models.CharField(null=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserConversationTechnique',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('Technique', models.ForeignKey(to='defaultapp.Technique')),
                ('conversation', models.ForeignKey(to='conversationmanager.Conversation')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='persistentnatconversation',
            name='technique',
            field=models.ForeignKey(to='defaultapp.Technique'),
        ),
        migrations.AddField(
            model_name='intermediatebeliefconversation',
            name='technique',
            field=models.ForeignKey(to='defaultapp.Technique'),
        ),
        migrations.AddField(
            model_name='eventlistconversation',
            name='technique',
            field=models.ForeignKey(to='defaultapp.Technique'),
        ),
        migrations.AddField(
            model_name='defaultconversation',
            name='technique',
            field=models.ForeignKey(to='defaultapp.Technique'),
        ),
        migrations.AddField(
            model_name='corebeliefconversation',
            name='technique',
            field=models.ForeignKey(to='defaultapp.Technique'),
        ),
    ]

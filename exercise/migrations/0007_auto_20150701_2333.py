# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0008_auto_20150701_2333'),
        ('exercise', '0006_auto_20150701_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationToConversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConversationToModule',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('module_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseConversation',
            fields=[
                ('conversationID', models.IntegerField(serialize=False, primary_key=True)),
                ('conversation_text', models.TextField()),
                ('conversation_type', models.CharField(max_length=255, default='Base')),
            ],
            options={
                'ordering': ['conversationID'],
            },
        ),
        migrations.AddField(
            model_name='conversationtomodule',
            name='conversationID',
            field=models.ForeignKey(null=True, related_name='conversation', to='exercise.ExerciseConversation'),
        ),
        migrations.AddField(
            model_name='conversationtomodule',
            name='correct_technique',
            field=models.ForeignKey(to='defaultapp.Technique'),
        ),
        migrations.AddField(
            model_name='conversationtoconversation',
            name='base_conversation',
            field=models.ForeignKey(null=True, related_name='base_conversation', to='exercise.ExerciseConversation'),
        ),
        migrations.AddField(
            model_name='conversationtoconversation',
            name='technique',
            field=models.ForeignKey(to='defaultapp.Technique'),
        ),
        migrations.AddField(
            model_name='conversationtoconversation',
            name='technique_conversation',
            field=models.ForeignKey(null=True, related_name='technique_conversation', to='exercise.ExerciseConversation'),
        ),
    ]

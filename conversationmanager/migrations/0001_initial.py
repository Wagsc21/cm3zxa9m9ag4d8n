# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversationoption',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversations',
            fields=[
                ('conversationID', models.IntegerField()),
                ('dialog', models.IntegerField(serialize=False, verbose_name='dialog', primary_key=True)),
                ('conversation_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('optionID', models.IntegerField(serialize=False, primary_key=True)),
                ('option_text', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['optionID'],
            },
        ),
        migrations.CreateModel(
            name='Userconversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('conversation_time', models.TimeField()),
                ('conversation', models.ForeignKey(to='conversationmanager.Conversations')),
                ('option_selected', models.ForeignKey(to='conversationmanager.Options')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['conversation_time', 'user'],
            },
        ),
        migrations.AddField(
            model_name='conversations',
            name='option',
            field=models.ManyToManyField(to='conversationmanager.Options', through='conversationmanager.Conversationoption'),
        ),
        migrations.AddField(
            model_name='conversations',
            name='user_conversation',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='conversationmanager.Userconversation'),
        ),
        migrations.AddField(
            model_name='conversationoption',
            name='crrent_conversation',
            field=models.ForeignKey(to='conversationmanager.Conversations'),
        ),
        migrations.AddField(
            model_name='conversationoption',
            name='next_converssation',
            field=models.ForeignKey(blank=True, to='conversationmanager.Conversations', related_name='next_convers', null=True),
        ),
        migrations.AddField(
            model_name='conversationoption',
            name='option',
            field=models.ForeignKey(to='conversationmanager.Options'),
        ),
    ]

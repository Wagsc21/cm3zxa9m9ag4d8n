# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversationmanager', '0011_auto_20150629_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversationoptiongraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dialogs',
            fields=[
                ('dialog', models.IntegerField(verbose_name='dialog ID', primary_key=True, serialize=False)),
                ('dialog_text', models.TextField()),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
            ],
            options={
                'ordering': ['dialog'],
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('optionID', models.IntegerField(primary_key=True, serialize=False)),
                ('option_text', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['optionID'],
            },
        ),
        migrations.CreateModel(
            name='Userconversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('conversation_time', models.DateTimeField()),
                ('conversation', models.ForeignKey(to='conversationmanager.Dialogs')),
                ('conversationID', models.ForeignKey(to='conversationmanager.Conversation')),
                ('option_selected', models.ForeignKey(to='conversationmanager.Options')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-conversation_time', 'user'],
            },
        ),
        migrations.AddField(
            model_name='dialogs',
            name='option',
            field=models.ManyToManyField(to='conversationmanager.Options', through='conversationmanager.Conversationoptiongraph'),
        ),
        migrations.AddField(
            model_name='dialogs',
            name='user_conversation',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='conversationmanager.Userconversation'),
        ),
        migrations.AddField(
            model_name='conversationoptiongraph',
            name='current_dialog',
            field=models.ForeignKey(to='conversationmanager.Dialogs'),
        ),
        migrations.AddField(
            model_name='conversationoptiongraph',
            name='next_dialog',
            field=models.ForeignKey(blank=True, related_name='next_conversation', null=True, to='conversationmanager.Dialogs'),
        ),
        migrations.AddField(
            model_name='conversationoptiongraph',
            name='option',
            field=models.ForeignKey(to='conversationmanager.Options'),
        ),
    ]

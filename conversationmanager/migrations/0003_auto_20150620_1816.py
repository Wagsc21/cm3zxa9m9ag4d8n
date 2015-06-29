# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversationmanager', '0002_auto_20150620_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversationoption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Conversations',
            fields=[
                ('conversationID', models.IntegerField()),
                ('dialog', models.IntegerField(verbose_name='dialog', primary_key=True, serialize=False)),
                ('conversation_text', models.TextField()),
            ],
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
            name='current_conversation',
            field=models.ForeignKey(to='conversationmanager.Conversations'),
        ),
        migrations.AddField(
            model_name='conversationoption',
            name='next_conversation',
            field=models.ForeignKey(null=True, related_name='next_conversation', blank=True, to='conversationmanager.Conversations'),
        ),
        migrations.AddField(
            model_name='conversationoption',
            name='option',
            field=models.ForeignKey(to='conversationmanager.Options'),
        ),
    ]

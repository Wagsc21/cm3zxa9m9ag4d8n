# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversationmanager', '0005_auto_20150625_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userconversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('conversation_time', models.DateTimeField()),
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
            name='user_conversation',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='conversationmanager.Userconversation'),
        ),
    ]

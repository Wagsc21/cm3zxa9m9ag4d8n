# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_auto_20150628_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationToConversation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('technique', models.CharField(max_length=255)),
                ('base_conversation', models.ForeignKey(null=True, to='exercise.ExerciseConversation', related_name='base_conversation')),
                ('technique_conversation', models.ForeignKey(null=True, to='exercise.ExerciseConversation', related_name='technique_conversation')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_conversationtoconversation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationToModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('module_number', models.IntegerField()),
                ('correct_technique', models.CharField(null=True, max_length=255)),
                ('conversation', models.ForeignKey(null=True, to='exercise.ExerciseConversation', related_name='conversation')),
            ],
        ),
        migrations.AlterField(
            model_name='conversationtoconversation',
            name='technique',
            field=models.CharField(null=True, max_length=255),
        ),
    ]

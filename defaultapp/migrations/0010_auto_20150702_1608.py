# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0015_conversationhistory'),
        ('cbt2', '0009_auto_20150702_1608'),
        ('defaultapp', '0009_auto_20150702_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationTechniqueBeliefsEventsNats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('beliefseventsnats', models.ForeignKey(to='cbt2.BeliefsEventsNats')),
                ('conversation', models.OneToOneField(to='conversationmanager.Conversation')),
                ('technique', models.ForeignKey(to='defaultapp.Technique')),
            ],
        ),
        migrations.CreateModel(
            name='ShowTechniqueBeliefsEventsNats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('beliefseventsnats', models.ForeignKey(to='cbt2.BeliefsEventsNats')),
                ('technique', models.ForeignKey(to='defaultapp.Technique')),
            ],
        ),
        migrations.RenameField(
            model_name='userconversationtechnique',
            old_name='Technique',
            new_name='technique',
        ),
        migrations.AlterUniqueTogether(
            name='userconversationtechnique',
            unique_together=set([('user', 'technique', 'conversation')]),
        ),
        migrations.AlterUniqueTogether(
            name='showtechniquebeliefseventsnats',
            unique_together=set([('technique', 'beliefseventsnats')]),
        ),
        migrations.AlterUniqueTogether(
            name='conversationtechniquebeliefseventsnats',
            unique_together=set([('technique', 'beliefseventsnats', 'conversation')]),
        ),
    ]

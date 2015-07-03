# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0009_auto_20150702_1430'),
        ('cbt2', '0007_auto_20150701_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corebelief',
            name='corebeliefs',
        ),
        migrations.RemoveField(
            model_name='eventlist',
            name='event',
        ),
        migrations.RemoveField(
            model_name='intermediatebelief',
            name='intermediatebeliefs',
        ),
        migrations.RemoveField(
            model_name='persistentnat',
            name='persistentnats',
        ),
        migrations.RemoveField(
            model_name='userevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='userevent',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userpnat',
            name='persistentnat',
        ),
        migrations.RemoveField(
            model_name='userpnat',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userscb',
            name='corebelief',
        ),
        migrations.RemoveField(
            model_name='userscb',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usersib',
            name='intermediatebelief',
        ),
        migrations.RemoveField(
            model_name='usersib',
            name='user',
        ),
        migrations.DeleteModel(
            name='Corebelief',
        ),
        migrations.DeleteModel(
            name='Eventlist',
        ),
        migrations.DeleteModel(
            name='Intermediatebelief',
        ),
        migrations.DeleteModel(
            name='Persistentnat',
        ),
        migrations.DeleteModel(
            name='Userevent',
        ),
        migrations.DeleteModel(
            name='Userpnat',
        ),
        migrations.DeleteModel(
            name='Userscb',
        ),
        migrations.DeleteModel(
            name='Usersib',
        ),
    ]

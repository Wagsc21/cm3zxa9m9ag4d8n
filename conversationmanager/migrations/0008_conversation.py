# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0007_auto_20150625_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('conversationID', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
    ]

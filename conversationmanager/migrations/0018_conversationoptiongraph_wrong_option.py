# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0017_auto_20150705_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationoptiongraph',
            name='wrong_option',
            field=models.BooleanField(default=False),
        ),
    ]

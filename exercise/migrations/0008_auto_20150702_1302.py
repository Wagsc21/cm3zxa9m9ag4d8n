# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0007_auto_20150701_2333'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='conversationtoconversation',
            unique_together=set([('base_conversation', 'technique')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversationmanager', '0015_conversationhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialogs',
            name='user_conversation',
        ),
    ]

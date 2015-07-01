# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0004_auto_20150628_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationtomodule',
            old_name='conversation',
            new_name='conversationID',
        ),
    ]

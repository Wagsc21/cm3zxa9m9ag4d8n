# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0009_challengenat_identifynat_modifyingbelief'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identifynat',
            old_name='Technique',
            new_name='technique',
        ),
    ]

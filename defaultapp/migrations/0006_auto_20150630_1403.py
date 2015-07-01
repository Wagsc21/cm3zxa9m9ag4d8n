# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defaultapp', '0005_corebeliefconversation_eventlistconversation_persistentnatconversation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corebeliefconversation',
            old_name='intermediatebelief',
            new_name='corebelief',
        ),
        migrations.RenameField(
            model_name='eventlistconversation',
            old_name='intermediatebelief',
            new_name='eventlist',
        ),
        migrations.RenameField(
            model_name='persistentnatconversation',
            old_name='intermediatebelief',
            new_name='persistentnat',
        ),
    ]

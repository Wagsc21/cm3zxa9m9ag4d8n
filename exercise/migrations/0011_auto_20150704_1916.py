# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0010_auto_20150704_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challengenat',
            name='user',
        ),
        migrations.RemoveField(
            model_name='identifynat',
            name='user',
        ),
        migrations.RemoveField(
            model_name='modifyingbelief',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChallengeNat',
        ),
        migrations.DeleteModel(
            name='IdentifyNat',
        ),
        migrations.DeleteModel(
            name='ModifyingBelief',
        ),
    ]

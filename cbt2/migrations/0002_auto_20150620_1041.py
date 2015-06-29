# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbt2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersprofile',
            name='agegroup',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='enrolled_as',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='userprofileID',
        ),
        migrations.DeleteModel(
            name='UsersProfile',
        ),
    ]

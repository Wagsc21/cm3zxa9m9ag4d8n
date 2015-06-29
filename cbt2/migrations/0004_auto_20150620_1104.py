# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbt2', '0003_customeuserprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customeuserprofile',
            name='agegroup',
        ),
        migrations.RemoveField(
            model_name='customeuserprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='customeuserprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customeuserprofile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='customeuserprofile',
            name='enrolled_as',
        ),
        migrations.RemoveField(
            model_name='customeuserprofile',
            name='userprofileID',
        ),
        migrations.RemoveField(
            model_name='test',
            name='usertestID',
        ),
        migrations.DeleteModel(
            name='Age',
        ),
        migrations.DeleteModel(
            name='Avatars',
        ),
        migrations.DeleteModel(
            name='Countries',
        ),
        migrations.DeleteModel(
            name='Customeuser',
        ),
        migrations.DeleteModel(
            name='Customeuserprofile',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Occupations',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]

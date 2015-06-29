# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbt2', '0002_auto_20150620_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customeuserprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('gender', models.CharField(max_length=10, choices=[('female', 'FEMALE'), ('male', 'MALE'), ('other', 'OTHER')])),
                ('phonenumber', models.CharField(max_length=10)),
                ('agegroup', models.ForeignKey(to='cbt2.Age')),
                ('avatar', models.ForeignKey(to='cbt2.Avatars', default=1)),
                ('country', models.ForeignKey(to='cbt2.Countries')),
                ('education', models.ForeignKey(to='cbt2.Education')),
                ('enrolled_as', models.ForeignKey(to='cbt2.Occupations')),
                ('userprofileID', models.OneToOneField(to='cbt2.Customeuser')),
            ],
        ),
    ]

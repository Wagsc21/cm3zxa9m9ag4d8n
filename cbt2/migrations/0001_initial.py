# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('agegroupID', models.AutoField(primary_key=True, serialize=False)),
                ('agegroup', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['agegroupID'],
            },
        ),
        migrations.CreateModel(
            name='Avatars',
            fields=[
                ('avatarID', models.IntegerField(primary_key=True, serialize=False)),
                ('avatarImage', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('countryID', models.IntegerField(primary_key=True, serialize=False)),
                ('country_Name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['country_Name'],
            },
        ),
        migrations.CreateModel(
            name='Customeuser',
            fields=[
                ('users_account_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('educationID', models.IntegerField(primary_key=True, serialize=False)),
                ('education_qualification', models.CharField(null=True, blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Occupations',
            fields=[
                ('occupationID', models.AutoField(primary_key=True, serialize=False)),
                ('occupation_name', models.CharField(null=True, blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('dsasweek1', models.CharField(null=True, blank=True, max_length=50)),
                ('dsasweek2', models.CharField(null=True, blank=True, max_length=50)),
                ('dsasweek3', models.CharField(null=True, blank=True, max_length=50)),
                ('dsasweek4', models.CharField(null=True, blank=True, max_length=50)),
                ('dsasweek5', models.CharField(null=True, blank=True, max_length=50)),
                ('asweek1', models.CharField(null=True, blank=True, max_length=50)),
                ('asweek2', models.CharField(null=True, blank=True, max_length=50)),
                ('asweek3', models.CharField(null=True, blank=True, max_length=50)),
                ('asweek4', models.CharField(null=True, blank=True, max_length=50)),
                ('asweek5', models.CharField(null=True, blank=True, max_length=50)),
                ('usertestID', models.ForeignKey(to='cbt2.Customeuser')),
            ],
        ),
        migrations.CreateModel(
            name='UsersProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('gender', models.CharField(max_length=10, choices=[('female', 'FEMALE'), ('male', 'MALE'), ('other', 'OTHER')])),
                ('phonenumber', models.CharField(max_length=10)),
                ('agegroup', models.ForeignKey(to='cbt2.Age')),
                ('avatar', models.ForeignKey(default=1, to='cbt2.Avatars')),
                ('country', models.ForeignKey(to='cbt2.Countries')),
                ('education', models.ForeignKey(to='cbt2.Education')),
                ('enrolled_as', models.ForeignKey(to='cbt2.Occupations')),
                ('userprofileID', models.OneToOneField(to='cbt2.Customeuser')),
            ],
        ),
    ]

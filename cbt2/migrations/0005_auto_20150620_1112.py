# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cbt2', '0004_auto_20150620_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('agegroupID', models.AutoField(serialize=False, primary_key=True)),
                ('agegroup', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['agegroupID'],
            },
        ),
        migrations.CreateModel(
            name='Avatars',
            fields=[
                ('avatarID', models.IntegerField(serialize=False, primary_key=True)),
                ('avatarImage', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('countryID', models.IntegerField(serialize=False, primary_key=True)),
                ('country_Name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['country_Name'],
            },
        ),
        migrations.CreateModel(
            name='Customuserprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('gender', models.CharField(choices=[('female', 'FEMALE'), ('male', 'MALE'), ('other', 'OTHER')], max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('agegroup', models.ForeignKey(to='cbt2.Age')),
                ('avatar', models.ForeignKey(default=1, to='cbt2.Avatars')),
                ('country', models.ForeignKey(to='cbt2.Countries')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('educationID', models.IntegerField(serialize=False, primary_key=True)),
                ('education_qualification', models.CharField(blank=True, null=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Occupations',
            fields=[
                ('occupationID', models.AutoField(serialize=False, primary_key=True)),
                ('occupation_name', models.CharField(blank=True, null=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('dsasweek1', models.CharField(blank=True, null=True, max_length=50)),
                ('dsasweek2', models.CharField(blank=True, null=True, max_length=50)),
                ('dsasweek3', models.CharField(blank=True, null=True, max_length=50)),
                ('dsasweek4', models.CharField(blank=True, null=True, max_length=50)),
                ('dsasweek5', models.CharField(blank=True, null=True, max_length=50)),
                ('asweek1', models.CharField(blank=True, null=True, max_length=50)),
                ('asweek2', models.CharField(blank=True, null=True, max_length=50)),
                ('asweek3', models.CharField(blank=True, null=True, max_length=50)),
                ('asweek4', models.CharField(blank=True, null=True, max_length=50)),
                ('asweek5', models.CharField(blank=True, null=True, max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuserprofile',
            name='education',
            field=models.ForeignKey(to='cbt2.Education'),
        ),
        migrations.AddField(
            model_name='customuserprofile',
            name='enrolled_as',
            field=models.ForeignKey(to='cbt2.Occupations'),
        ),
        migrations.AddField(
            model_name='customuserprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]

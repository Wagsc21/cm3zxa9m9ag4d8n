# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cbt2', '0005_auto_20150620_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corebelief',
            fields=[
                ('corebeliefID', models.IntegerField(serialize=False, primary_key=True)),
                ('corebelief_text', models.TextField()),
            ],
            options={
                'ordering': ['corebeliefID'],
            },
        ),
        migrations.CreateModel(
            name='Eventlist',
            fields=[
                ('eventID', models.IntegerField(serialize=False, primary_key=True)),
                ('event_text', models.TextField()),
            ],
            options={
                'ordering': ['eventID'],
            },
        ),
        migrations.CreateModel(
            name='Familymembers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('member_name', models.CharField(verbose_name='Name', max_length=200)),
                ('relate', models.CharField(default='', verbose_name='Relation to you', max_length=50)),
                ('emailid', models.EmailField(blank=True, verbose_name='Email ID', max_length=25, null=True)),
                ('phonenumber', models.CharField(blank=True, verbose_name='Phone Number', max_length=10, null=True)),
                ('involvementid', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intermediatebelief',
            fields=[
                ('intermediatebeliefID', models.IntegerField(serialize=False, primary_key=True)),
                ('intermediatebelief_text', models.TextField()),
            ],
            options={
                'ordering': ['intermediatebeliefID'],
            },
        ),
        migrations.CreateModel(
            name='Persistentnat',
            fields=[
                ('persistentnatID', models.IntegerField(serialize=False, primary_key=True)),
                ('persistentnat_text', models.TextField()),
            ],
            options={
                'ordering': ['persistentnatID'],
            },
        ),
        migrations.CreateModel(
            name='Userevent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('chaeck', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='cbt2.Eventlist')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userpnat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('persistentnat', models.ForeignKey(to='cbt2.Persistentnat')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userscb',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('corebelief', models.ForeignKey(to='cbt2.Corebelief')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usersib',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('intermediatebelief', models.ForeignKey(to='cbt2.Intermediatebelief')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='persistentnat',
            name='persistentnats',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cbt2.Userpnat'),
        ),
        migrations.AddField(
            model_name='intermediatebelief',
            name='intermediatebeliefs',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cbt2.Usersib'),
        ),
        migrations.AddField(
            model_name='eventlist',
            name='event',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cbt2.Userevent'),
        ),
        migrations.AddField(
            model_name='corebelief',
            name='corebeliefs',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cbt2.Userscb'),
        ),
    ]

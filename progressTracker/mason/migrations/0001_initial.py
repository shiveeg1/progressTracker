# -*- coding: utf-8 -*-

# Generated by Django 1.11.4 on 2017-08-03 19:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='brick',
            fields=[
                ('brickId', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=400)),
                ('desc', models.CharField(max_length=1000)),
                ('proofUrl', models.URLField()),
                ('imgPath', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'brick',
            },
        ),
        migrations.CreateModel(
            name='brickType',
            fields=[
                ('brickTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1000)),
                ('imgPAth', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'brickType',
            },
        ),
        migrations.CreateModel(
            name='constructionProject',
            fields=[
                ('upvId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('brickQty', models.IntegerField()),
                ('constnFreq', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'constructionProject',
            },
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('groupId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('code', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='pillar',
            fields=[
                ('pillarId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('imgPath', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pillar',
            },
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('roleId', models.AutoField(primary_key=True, serialize=False)),
                ('masonName', models.CharField(max_length=50)),
                ('masonBonus', models.IntegerField()),
                ('superPowers', models.CharField(max_length=200)),
                ('imgPath', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='skillLevel',
            fields=[
                ('skillId', models.AutoField(primary_key=True, serialize=False)),
                ('numOfBricks', models.IntegerField()),
                ('steakCount', models.IntegerField()),
            ],
            options={
                'db_table': 'skillLevel',
            },
        ),
        migrations.CreateModel(
            name='userGroupDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.group')),
                ('pillar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.pillar')),
            ],
            options={
                'db_table': 'userGroupDetails',
            },
        ),
        migrations.CreateModel(
            name='userMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePicUrl', models.CharField(max_length=100)),
                ('currRole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userMetadata',
            },
        ),
        migrations.CreateModel(
            name='userProject',
            fields=[
                ('upId', models.AutoField(primary_key=True, serialize=False)),
                ('constnStartDate', models.DateTimeField(default=datetime.datetime(2017, 8, 3, 19, 48, 58, 648010, tzinfo=utc))),
                ('constnEndDate', models.DateTimeField()),
                ('skillLevelStartDate', models.DateField()),
                ('currentVersion', models.IntegerField()),
                ('brickType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.brickType')),
                ('pillar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.pillar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.userMetadata')),
            ],
            options={
                'db_table': 'userProject',
            },
        ),
        migrations.CreateModel(
            name='workSprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('brickQty', models.IntegerField()),
                ('actionMetadata', models.CommaSeparatedIntegerField(max_length=500)),
                ('brickType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.brick')),
                ('cpId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.constructionProject')),
            ],
            options={
                'db_table': 'workSprint',
            },
        ),
        migrations.AddField(
            model_name='usergroupdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mason.userMetadata'),
        ),
    ]

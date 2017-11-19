# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=250)),
                ('edate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('idno', models.CharField(max_length=400)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extropy.Event')),
            ],
        ),
    ]

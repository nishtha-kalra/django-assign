# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_name', models.CharField(max_length=50)),
                ('phone_number', models.PositiveIntegerField(max_length=10)),
                ('address', models.CharField(max_length=300)),
                ('alt_number', models.PositiveIntegerField(max_length=10)),
            ],
        ),
    ]

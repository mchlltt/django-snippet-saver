# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-09 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('language', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('description', models.TextField(max_length=256)),
            ],
        ),
    ]

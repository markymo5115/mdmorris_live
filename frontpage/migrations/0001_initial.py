# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Introduction',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0004_auto_20171030_1652'),
        ('zinnia_gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='pictures',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]

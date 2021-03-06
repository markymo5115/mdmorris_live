# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isProjectGallery', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Extra fields',
                'verbose_name': 'Extra fields',
            },
        ),
        migrations.CreateModel(
            name='MyGallery',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('photologue.gallery',),
        ),
        migrations.CreateModel(
            name='MyPhoto',
            fields=[
            ],
            options={
                'proxy': True,
                'ordering': ['date_added'],
            },
            bases=('photologue.photo',),
        ),
        migrations.AddField(
            model_name='galleryextended',
            name='gallery',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended', to='photologue.Gallery'),
        ),
        migrations.AddField(
            model_name='galleryextended',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

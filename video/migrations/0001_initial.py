# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_playlist', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('likes', models.IntegerField(default=0)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Playlist')),
            ],
        ),
    ]

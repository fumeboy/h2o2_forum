# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 14:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import threads.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('threads', '0001_initial'),
        ('boards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=models.SET(threads.models.get_null_user), related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='board',
            field=models.ForeignKey(on_delete=models.SET(threads.models.get_null_board), related_name='posts', to='boards.Board'),
        ),
    ]

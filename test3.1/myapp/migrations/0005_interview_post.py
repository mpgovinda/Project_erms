# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-04 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20160704_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='Post',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='myapp.Post'),
            preserve_default=False,
        ),
    ]

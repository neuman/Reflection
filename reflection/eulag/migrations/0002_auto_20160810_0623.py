# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-10 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eulag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consent',
            name='terms',
        ),
        migrations.RemoveField(
            model_name='consent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='termsheet',
            name='owners',
        ),
        migrations.AddField(
            model_name='consent',
            name='termsheet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eulag.TermSheet'),
        ),
    ]

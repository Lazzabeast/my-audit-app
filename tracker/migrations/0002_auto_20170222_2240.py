# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='owner',
            field=models.CharField(default='n/a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evidence',
            name='required_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evidence',
            name='system',
            field=models.CharField(default='n/a', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evidence',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
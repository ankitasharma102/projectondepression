# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20170623_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='Time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

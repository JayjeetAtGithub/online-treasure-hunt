# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 09:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0003_auto_20180128_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='audio1',
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 1, 28, 15, 26, 39, 946611)),
        ),
    ]

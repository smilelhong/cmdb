# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-04 10:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='apply_time',
            field=models.DateField(default=datetime.datetime(2018, 3, 4, 18, 48, 11, 122000), verbose_name='申请时间'),
        ),
        migrations.AlterField(
            model_name='iprange',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2018, 3, 4, 18, 48, 11, 122000), verbose_name='创建时间'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='登录时间'),
        ),
    ]

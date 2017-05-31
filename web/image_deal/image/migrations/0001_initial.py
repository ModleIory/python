# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=50, verbose_name='图片描述')),
                ('url', models.CharField(max_length=300, verbose_name='储存路径')),
                ('uid', models.IntegerField(verbose_name='用户id')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='修改的时间')),
            ],
        ),
    ]

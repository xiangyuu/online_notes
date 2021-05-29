# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2021-05-13 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='用戶名')),
                ('password', models.CharField(max_length=30, verbose_name='密碼')),
            ],
        ),
    ]

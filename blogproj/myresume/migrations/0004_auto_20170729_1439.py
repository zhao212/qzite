# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0003_auto_20170729_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='res_education',
            name='degree',
            field=models.CharField(max_length=150, verbose_name='degree'),
        ),
        migrations.AlterField(
            model_name='res_education',
            name='major',
            field=models.CharField(blank=True, max_length=150, verbose_name='Major'),
        ),
    ]

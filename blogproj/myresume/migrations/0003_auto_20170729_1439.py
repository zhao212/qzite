# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 21:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myresume', '0002_res_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='res_award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=100, verbose_name='award')),
                ('get_year', models.DateField(default=django.utils.timezone.now, verbose_name='year')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='res_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=150, verbose_name='project name')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(verbose_name='project description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='res_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100, verbose_name='skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='res_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=150, verbose_name='title')),
                ('company_name', models.CharField(max_length=150, verbose_name='company')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(verbose_name='project description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='res_basic',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='res_basic',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='res_basic',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='res_education',
            name='degree',
            field=models.CharField(default='BS', max_length=150, verbose_name='degree'),
        ),
        migrations.AddField(
            model_name='res_education',
            name='major',
            field=models.CharField(blank=True, default='EE', max_length=150, verbose_name='Major'),
        ),
        migrations.AlterField(
            model_name='res_basic',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='res_basic',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='res_education',
            name='education_name',
            field=models.CharField(max_length=150, verbose_name='school'),
        ),
    ]

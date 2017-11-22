# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171118_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAnalytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Google Analytics Code',
                'verbose_name_plural': 'Google Analytics Code',
            },
        ),
        migrations.CreateModel(
            name='SiteTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Site Title',
                'verbose_name_plural': 'Site Title',
            },
        ),
    ]

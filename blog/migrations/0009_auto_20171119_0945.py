# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171118_1605'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GoogleAnalytics',
        ),
        migrations.DeleteModel(
            name='SiteTitle',
        ),
    ]

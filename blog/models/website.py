#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
from __future__ import unicode_literals

from django.db import models


class SiteTitle(models.Model):
    """Title/Name of the Blog
    """
    class Meta:
        verbose_name = "Site Title"
        verbose_name_plural = "Site Title"
        # app_label = "website"
        # db_table = "website_sitetitle"

    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class GoogleAnalytics(models.Model):
    """Google Analytics Code
    """
    class Meta:
        verbose_name = "Google Analytics Tracking Code"
        verbose_name_plural = "Google Analytics Tracking Code"
        # app_label = "website"
        # db_table = "website_googleanalytics"

    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name



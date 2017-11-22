#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
from blog.models.app import TemplateDir, User, Tag, Category
from blog.models.website import SiteTitle, GoogleAnalytics


def site_title(request):
    site_title = SiteTitle.objects.first().name if SiteTitle.objects.first() else ""
    return {'site_title': site_title}

def template_dir(request):
    template_dir = TemplateDir.get_name() if TemplateDir.objects.first() else ""
    return {'template_dir': template_dir}

def google_analytics(request):
    ga_tracking_code = GoogleAnalytics.objects.first().name if GoogleAnalytics.objects.first() else ""
    return {'ga_tracking_code': ga_tracking_code}

def authors(request):
    return { 'authors': User.objects.all() }

def tags(request):
    return { 'tags': Tag.objects.all() }

def categories(request):
    return { 'categories': Category.objects.all() }

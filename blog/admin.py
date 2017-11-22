#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from blog.models.app import Post, Tag, Category, TemplateDir
from blog.models.website import SiteTitle, GoogleAnalytics
from forms import TemplateDirForm

@admin.register(TemplateDir)
class TemplateAdmin(ModelAdmin):
    form = TemplateDirForm
    list_display = ['name', 'is_current']
    list_editable = ['is_current']


@admin.register(SiteTitle)
class SiteTitleAdmin(ModelAdmin):
    def has_add_permission(self, request):
        count = SiteTitle.objects.all().count()
        if count == 0:
            return True

        return False

@admin.register(GoogleAnalytics)
class GoogleAnalyticsAdmin(ModelAdmin):
    def has_add_permission(self, request):
        count = GoogleAnalytics.objects.all().count()
        if count == 0:
            return True

        return False


# Blog
admin.site.register(Post, ModelAdmin)
admin.site.register(Tag, ModelAdmin)
admin.site.register(Category, ModelAdmin)
# admin.site.register(TemplateDir, TemplateAdmin)

# set the admin titles
admin.site.site_header = 'Blue Jackal Site Admin'
admin.site.site_title = 'Site Administration'
admin.site.index_title = 'Blue Jackal'
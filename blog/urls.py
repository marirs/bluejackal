#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
from django.conf.urls import url
from blog.views import PostSearchView, ContactView, LatestPostsFeed
from views import PostDetailView, PostListView
from django.contrib.auth.views import logout
from django.conf.urls.static import static

from bluejackal import settings

urlpatterns = [
    url(r'^search/?$', PostSearchView.as_view(), name='search_view'),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^feeds/$', LatestPostsFeed(), name='feeds'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^account/logout/$',view=logout,name='tf_logout'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

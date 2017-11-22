#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
from haystack import indexes
from .models.app import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

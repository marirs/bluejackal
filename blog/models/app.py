#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from django.db.models.query_utils import Q
from django.urls.base import reverse


class Tag(models.Model):
    """Tags
    """
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        app_label = "blog"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Category
    """
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        app_label = "blog"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Posts
    """
    specialChars = '!@#$%^&*()[]{};:,./<>?\|`~=_-+"'+"'"

    class Meta:
        ordering = ['-created']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        app_label = "blog"

    author = models.ForeignKey(to=User, related_name='posts')
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=300, null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='posts')
    categories = models.ManyToManyField(to=Category, related_name='posts')
    body = RichTextField(config_name='ckadvanced')
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    @property
    def detail_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        slug = self.title.lower() if not self.slug else self.slug.lower()
        slug = slug.translate({ord(c): "" for c in self.specialChars})
        self.slug =slug.replace(' ', '-')
        super(Post, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title


class TemplateDir(models.Model):
    """Templates Directory
    """
    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"
        app_label = "blog"

    name = models.CharField(max_length=100)
    is_current = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_current:
            TemplateDir.objects.filter(~Q(id=self.id)).update(is_current=False)
        return super(TemplateDir, self).save(*args, **kwargs)

    @staticmethod
    def get_name():
        try:
            return TemplateDir.objects.filter(is_current=True)[0].name
        except:
            return TemplateDir.objects.first().name

    def __str__(self):
        return self.name






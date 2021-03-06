#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.syndication.views import Feed
from django.urls import reverse
# Create your views here.
from django.utils.html import strip_tags
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from el_pagination.settings import PAGE_LABEL
from el_pagination.views import AjaxListView
from haystack.generic_views import SearchView

from blog.forms import ContactForm
from blog.models.app import Post, TemplateDir
from blog.models.website import SiteTitle


class PostListView(AjaxListView):
    model = Post

    def get_template_name(self):
        return '{}/blog/post_list.html'.format(TemplateDir.get_name())

    def get_page_template(self, **kwargs):
        return '{}/blog/post_list_page.html'.format(TemplateDir.get_name())

    def get_template_names(self):
        """Switch the templates for Ajax requests."""
        request = self.request
        key = 'querystring_key'
        querystring_key = request.GET.get(key,
            request.POST.get(key, PAGE_LABEL))
        if request.is_ajax() and querystring_key == self.key:
            return [self.get_page_template()]
        return [self.get_template_name()]

    def get_queryset(self):
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        author = self.request.GET.get('author')
        author_fn = self.request.GET.get('name')
        if category:
            return Post.objects.filter(categories__name__contains=category)
        if tag:
            return Post.objects.filter(tags__name__contains=tag)
        if author:
            return Post.objects.filter(author__username=author)
        if author_fn:
            return Post.objects.filter(author__first_name=author_fn)
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(published=True)

    def get_template_names(self):
        return ['{}/blog/post_detail.html'.format(TemplateDir.get_name())]


class PostSearchView(SearchView):

    def get_template_names(self):
        return ['{}/search/search.html'.format(TemplateDir.get_name())]


class ContactView(FormView):
    form_class = ContactForm
    success_url = '/?contact_submitted'

    def get_template_names(self, *args, **kwargs):
        return ['{}/blog/contact.html'.format(TemplateDir.get_name())]


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)


class LatestPostsFeed(Feed):
    link = "/feeds/"

    try:
        title = SiteTitle.objects.first().name
    except AttributeError:
        title = 'Blog powered by BlueJackal'

    def items(self):
        return Post.objects.order_by('-created')[:settings.FEED_NUM_ITEMS]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse('post_detail', args=[item.slug])

    def item_description(self, item):
        body = strip_tags(item.body)
        return body[:settings.FEED_DESC_MAX_LENGTH] + '...' if len(body) > settings.FEED_DESC_MAX_LENGTH else body

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_author_email(self, item):
        return item.author.email

    def item_categories(self, item):
        return item.categories.values_list('name', flat=True)

    def item_pubdate(self, item):
        return item.created

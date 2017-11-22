#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
from django import forms
from django.forms import ModelForm
from captcha.fields import CaptchaField
from django.core.mail import send_mail
from django.conf import settings

import os

class ContactForm(forms.Form):
    """Contact form
    """
    name = forms.CharField(max_length=50, required=True)
    company = forms.CharField(max_length=50, required=False)
    website = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=400, required=True, min_length=10)
    captcha = CaptchaField(required=True)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for fname, field in self.fields.iteritems():
            field.widget.attrs['class'] = 'form-control'


    def send_email(self):
        body = 'Name: {} <br/>'.format(self.cleaned_data.get('name')) + \
               'Company: {} <br/>'.format(self.cleaned_data.get('company')) + \
               'Website: {} <br/>'.format(self.cleaned_data.get('website')) + \
               self.cleaned_data.get('message')
        send_mail(subject='Feedback', message='', from_email=self.cleaned_data.get('email'),
                  recipient_list=settings.ADMIN_EMAILS, fail_silently=True, html_message=body)



class TemplateDirForm(ModelForm):
    """Dropdown form for showing available templates
    """
    name = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
       super(TemplateDirForm, self).__init__(*args, **kwargs)
       self.fields['name'].choices = self.get_template_folders()

    def get_template_folders(self, target_path=os.path.join(os.getcwd(),'blog/templates/')):
        dir_contents = os.listdir(target_path)
        directories = []
        for item in dir_contents:
            if os.path.isdir(''.join((target_path, item,))):
                if item != "search" and item != "two_factor" and item != "admin":
                    directories.append((item, item), )
        folder_list = tuple(directories)
        return folder_list


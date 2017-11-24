#!/usr/bin/env python
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""

SITE_ID = 1

# for production systems use debug as false
DEBUG = True

# setting the allowed_hosts deters from cache poisoning, host parsing, etc,.
# it's possible to use wildcards in a project's settings, in which case this
# feature doesn't help secure anything.
ALLOWED_HOSTS = ['*']

# enter a comma seperated email addresses to receive any email
ADMIN_EMAILS = ['marirs@gmail.com']

# email host settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# reCaptcha v2 keys:
RECAPTCHA_PRIVATE_KEY = 'your private key'
RECAPTCHA_PUBLIC_KEY = 'your public key'



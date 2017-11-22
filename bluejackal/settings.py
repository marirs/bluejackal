#!/usr/bin/env python
"""
BlueJackal - Django CMS
Copyright (C) 2017 Blue Jackal.
This file is part of Blue Jackal Django CMS System.
See the file 'LICENSE' for copying permission.
"""
import os

SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '6x)t-kv^#r(#huz8584ohl8lwdp+@ak3-ghk^k(t^w#bbo$+^)'

POSTS_PER_PAGE = 3

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'user_sessions',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'activelink',
    'ckeditor',
    'el_pagination',
    'haystack',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'captcha',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'user_sessions.middleware.SessionMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bluejackal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 # custom context processors
                'bluejackal.template.context_processors.site_title',        # head <title>
                'bluejackal.template.context_processors.google_analytics',  # google analytics tracking code: eg: UA-xx
                'bluejackal.template.context_processors.template_dir',      # template directory
                'bluejackal.template.context_processors.authors',           # blog authors
                'bluejackal.template.context_processors.tags',              # blog tags
                'bluejackal.template.context_processors.categories',        # blog categories
            ],
        'libraries':{
            'base_extras': 'blog.templatetags.base_extras',

            }
        },
    },
]

WSGI_APPLICATION = 'bluejackal.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database/bluejackal.sqlite3'),
    }
}

SESSION_ENGINE = 'user_sessions.backends.db'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'blog/static/')

CKEDITOR_CONFIGS = {
    'ckadvanced': {
        'toolbar': 'Advanced',
    },
}

EL_PAGINATION_PER_PAGE = POSTS_PER_PAGE
EL_PAGINATION_PAGE_LABEL = 'next'
EL_PAGINATION_LOADING = 'getting more posts'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index')
    },
}

INTERNAL_IPS = ('127.0.0.1',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'two_factor': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

ADMIN_EMAILS = []

EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

#two factor setting
LOGIN_URL = 'two_factor:login'
LOGOUT_REDIRECT_URL = 'post_list'
LOGIN_REDIRECT_URL = 'post_list'

TWO_FACTOR_PATCH_ADMIN = True

# geoip2 datasets path
GEOIP_PATH = os.path.join(BASE_DIR, 'database/geoip2/')

# Import local settings.
execfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "user_settings.py"), globals(), locals())

# -*- coding: utf-8 -*-

"""
__init__.py
Crée par Flavien-hugs - 2019/12/05/.
Copyright (c) 2019 unsta. All rights reserved.
"""

import dj_database_url
from yapp.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# 'django.middleware.security.SecurityMiddleware',
MIDDLEWARE += [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ALLOWED_HOSTS = ['unsta-youtube.herokuapp.com']

# APPLICATION DEFINITION
INSTALLED_APPS += ['whitenoise.runserver_nostatic']

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

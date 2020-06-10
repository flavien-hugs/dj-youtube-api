# -*- coding: utf-8 -*-

"""
__init__.py

Crée par Flavien-hugs - 2019/12/05/.
Copyright (c) 2019 unsta. All rights reserved.

"""
__author__ = 'Flavien-hugs <flavienhugs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta projet youtube_api_search'


import os
import sys
import os.path
from whitenoise.django import DjangoWhiteNoise

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'yapp')))

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yapp.settings')
application = get_wsgi_application()
application = DjangoWhiteNoise(application)

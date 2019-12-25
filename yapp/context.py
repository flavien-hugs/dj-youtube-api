# -*- coding: utf-8 -*-

"""
__init__.py

Crée par Flavien-hugs - 2019/12/05/.
Copyright (c) 2019 unsta. All rights reserved.

"""
__author__ = 'Flavien-hugs <flavienhugs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta projet youtube_api_search'

from yapp import settings

# Context processor
def yapp(request):
    return {
        'site_name': settings.SITE_NAME,
        'site_description': settings.SITE_DESCRIPTION,
        'meta_keyword' : settings.META_KEYWORDS,
        'request': request
    }

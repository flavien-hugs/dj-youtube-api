# -*- coding: utf-8 -*-

"""
__init__.py

Crée par Flavien-hugs - 2019/12/05/.
Copyright (c) 2019 unsta. All rights reserved.

"""
__author__ = 'Flavien-hugs <flavienhugs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta projet youtube_api_search'


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ysearch.urls', namespace='ysearch'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

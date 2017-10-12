# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from djangocms_slick_slider.urls import urlpatterns as djangocms_slick_slider_urls

urlpatterns = [
    url(r'^', include(djangocms_slick_slider_urls, namespace='djangocms_slick_slider')),
]

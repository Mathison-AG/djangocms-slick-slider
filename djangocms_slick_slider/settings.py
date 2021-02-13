#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings

from .templatetags.djangocms_slick_slider_utils import jsonify

# these are the default settings for the slider
# change to your needs, if you like to
SLIDER_DEFAULT_DICT = {
    'dots': True,
    'slidesToShow': 2,
    'mobileFirst': False,
    'slidesToScroll': 1,
    'autoplay': True,
    'autoplaySpeed': 1500
}

SLICK_SLICKER_DEFAULT_OPTIONS = getattr(settings,
                                        'SLICK_SLICKER_DEFAULT_OPTIONS',
                                        SLIDER_DEFAULT_DICT)

SLIDER_DEFAULT = jsonify(SLICK_SLICKER_DEFAULT_OPTIONS, safe=False)


def get_setting(name):
    """
    Return the setting corresponding to the `name` given.
    """
    default = {
        'SLICK_SLICKER_DEFAULT_OPTIONS':
        SLIDER_DEFAULT,
        'SLICK_SLIDER_ACE_THEME':
        getattr(settings, 'SLICK_SLIDER_ACE_THEME', 'json'),
        'SLICK_SLIDER_ACE_MODE':
        getattr(settings, 'SLICK_SLIDER_ACE_MODE', 'github'),
        'SLICK_SLIDER_CONTAINER_WIDTH':
        getattr(settings, 'SLICK_SLIDER_CONTAINER_WIDTH', 1200)
    }

    return default[name]

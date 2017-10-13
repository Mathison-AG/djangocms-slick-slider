# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .templatetags.djangocms_slick_slider_utils import jsonify


def get_setting(name):
    """
    Return the setting corresponding to the `name` given.
    """
    from django.conf import settings

    default = {
        'SLICK_SLIDER_VERSION': getattr(
            settings, 'SLICK_SLIDER_VERSION', '1.8.0'),

        'SLICK_SLICKER_DEFAULT_OPTIONS': getattr(
            settings, 'SLICK_SLICKER_DEFAULT_OPTIONS',
            jsonify(
                {
                    'dots': True,
                    'slidesToShow': 4,
                    'mobileFirst': False,
                    'slidesToScroll': 4,
                    'autoplay': True,
                    'autoplaySpeed': 1200
                }
            )
        ),
        'SLICK_SLIDER_ACE_THEME': getattr(
            settings, 'SLICK_SLIDER_ACE_THEME', 'json'),

        'SLICK_SLIDER_ACE_MODE': getattr(
            settings, 'SLICK_SLIDER_ACE_MODE', 'github'),

    }
    return default[name]

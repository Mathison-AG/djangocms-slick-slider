#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djangocms-slick-slider
------------

Tests for `djangocms-slick-slider` models module.
"""
from djangocms_helper.base_test import BaseTestCase

from djangocms_slick_slider import settings
from djangocms_slick_slider import apps

from ._factories import SliderFactory


class SlickSliderModelTests(BaseTestCase):

    def setUp(self):

        self.assertEqual(apps.DjangocmsSlickSliderConfig.name,
                         'djangocms_slick_slider')

        self.slider = SliderFactory.create()

    def test_string_repr(self):
        self.assertEqual(str(self.slider), "Test Slider")

    def test_settings_default(self):
        self.assertEqual(self.slider.settings, settings.SLIDER_DEFAULT)

    def tearDown(self):
        pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djangocms-slick-slider
------------

Tests for `djangocms-slick-slider` models module.
"""

from django.test import TestCase

from djangocms_slick_slider import models
from djangocms_slick_slider import settings


class TestDjangocms_slick_slider(TestCase):

    def setUp(self):
        self.slider = models.SlickSlider()
        self.slider.title = "Test Slider"

    def test_string_repr(self):
        self.assertEqual(str(self.slider), "Test Slider")

    def test_settings_default(self):
        self.assertEqual(self.slider.settings, settings.SLIDER_DEFAULT)

    def tearDown(self):
        pass

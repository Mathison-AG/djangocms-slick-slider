#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djangocms-slick-slider
------------

Tests for `djangocms-slick-slider` models module.
"""
import factory
from copy import deepcopy

from djangocms_helper.base_test import BaseTestCase

from djangocms_slick_slider import models
from djangocms_slick_slider import settings
from djangocms_slick_slider import apps


class SliderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SlickSlider

    title = 'Test Slider'


class SliderImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SlickSliderImage


class SlickSliderModelTests(BaseTestCase):

    def setUp(self):

        self.assertEqual(apps.DjangocmsSlickSliderConfig.name,
                         'djangocms_slick_slider')

        self.slider = SliderFactory.create()
        for n in range(1, 7):
            image = self.create_filer_image_object()
            slider_image = SliderImageFactory.create(
                id=n,
                image=image,
                slider_id=self.slider.id)
            self.assertEqual(str(slider_image), "test_file.jpg")

    def test_string_repr(self):
        self.assertEqual(str(self.slider), "Test Slider")

    def test_settings_default(self):
        self.assertEqual(self.slider.settings, settings.SLIDER_DEFAULT)

    def test_slider_images(self):
        self.assertEqual(self.slider.images.count(), 6)

    def test_slider_deepcopy(self):
        new_slider = SliderFactory.create()
        new_slider.copy_relations(self.slider)

        self.assertEqual(self.slider.images.count(), 6)
        self.assertEqual(new_slider.images.count(), 6)

    def tearDown(self):
        pass

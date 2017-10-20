#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djangocms-slick-slider
------------

Tests for `djangocms-slick-slider` models module.
"""
# import factory

# from django.test import TestCase

# from djangocms_slick_slider import models
# from djangocms_slick_slider import settings


# class SliderFactory(factory.Factory):
#     class Meta:
#         model = models.SlickSlider

#     title = 'Test Slider'


# class TestDjangocms_slick_slider(TestCase):

#     def setUp(self):
#         self.slider = SliderFactory.create()


#     def test_string_repr(self):
#         self.assertEqual(str(self.slider), "Test Slider")

#     def test_settings_default(self):
#         self.assertEqual(self.slider.settings, settings.SLIDER_DEFAULT)

#     def test_cmsplugins_render(self):


#     def tearDown(self):
#         pass


from django.test import TestCase
from django.test.client import RequestFactory

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from djangocms_slick_slider.cms_plugins import SlickSliderPlugin
from djangocms_slick_slider.models import SlickSlider


class SlickSliderPluginTests(TestCase):
    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SlickSliderPlugin,
            'de',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render(
            {},
            model_instance, None)
        # self.assertEqual(context['instance'], 'Test Slider')

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SlickSliderPlugin,
            'de',
        )
        renderer = ContentRenderer(request=RequestFactory())
        from sekizai.context import SekizaiContext
        html = renderer.render_plugin(model_instance, SekizaiContext())
        self.assertIn('id="slider-wrapper"', html)

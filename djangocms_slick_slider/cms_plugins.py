# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import SlickSlider, SlickSliderImage


@plugin_pool.register_plugin
class SlickSliderPlugin(CMSPluginBase):
    model = SlickSlider
    name = _('Slick Slider')
    render_template = 'djangocms_slick_slider/base.html'
    allow_children = True
    child_classes = ['SlickSliderImagePlugin', ]

    def render(self, context, instance, placeholder):
        context = super(SlickSliderPlugin, self).render(
            context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class SlickSliderImagePlugin(CMSPluginBase):
    render_template = 'djangocms_slick_slider/image.html'
    name = _('Slick Slider Image')
    model = SlickSliderImage
    require_parent = True
    parent_classes = ['SlickSliderPlugin', ]

    def render(self, context, instance, placeholder):
        context = super(SlickSliderImagePlugin, self).render(
            context, instance, placeholder)
        return context

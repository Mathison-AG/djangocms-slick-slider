# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.utils.translation import ugettext_lazy as _


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .admin import SlickerSliderAceMixin
from .models import SlickSlider, SlickSliderImage
from .settings import SLICK_SLIDER_VERSION


@plugin_pool.register_plugin
class SlickSliderPlugin(SlickerSliderAceMixin, CMSPluginBase):
    model = SlickSlider
    name = _('Slick Slider')
    render_template = 'djangocms_slick_slider/base.html'
    allow_children = True
    child_classes = ['SlickSliderImagePlugin', ]

    def render(self, context, instance, placeholder):
        context = super(SlickSliderPlugin, self).render(
            context, instance, placeholder)
        context['settings'] = self.get_settings()
        context['child_width'] = "{w}x{w}".format(
            w=int((1200 / (instance.settings['slidesToShow'])) * 1.5)
        )
        return context

    def get_settings(self):
        """
        Constrcut and return settings dictionary.
        """
        settings = {}
        settings['SLICK_SLIDER_VERSION'] = SLICK_SLIDER_VERSION
        return settings


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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .admin import SlickerSliderAceMixin
from .models import SlickSlider, SlickSliderImage
from .settings import get_setting


class SlickSliderImageInline(admin.TabularInline):
    model = SlickSliderImage
    extra = 1


@plugin_pool.register_plugin
class SlickSliderPlugin(SlickerSliderAceMixin, CMSPluginBase):
    model = SlickSlider
    name = _('Slick Slider')
    render_template = 'djangocms_slick_slider/base.html'
    cache = False
    inlines = [SlickSliderImageInline, ]

    def render(self, context, instance, placeholder):
        context = super(SlickSliderPlugin, self).render(
            context, instance, placeholder)
        images = instance.images.all()
        context.update({
            'images': images,
            'settings': self.get_settings(),
            'child_width': '{w}x{w}'.format(w=(
                int((1200 / (instance.settings['slidesToShow'])) * 1.5)
            ))
        })
        return context

    def get_settings(self):
        """
        Constrcut and return settings dictionary.
        """
        settings = {}
        settings['SLICK_SLIDER_VERSION'] = get_setting('SLICK_SLIDER_VERSION')
        return settings

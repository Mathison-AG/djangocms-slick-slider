# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, connection
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField

from cms.models.pluginmodel import CMSPlugin

from .settings import SLICK_SLICKER_DEFAULT_OPTIONS

if 'postgre' in connection.vendor:
    from django.contrib.postgres.fields import JSONField
else:
    try:
        from jsonfield import JSONField
    except ImportError:
        raise Exception('You need to have "jsonfield" installed: pip install '
                        'jsonfield')


@python_2_unicode_compatible
class SlickSlider(CMSPlugin):
    """
    Main Plugin Model for the slider.
    """
    title = models.CharField(
        verbose_name=_('Slider title'),
        max_length=255)

    settings = JSONField(
        verbose_name=_('Slick settings'),
        default=SLICK_SLICKER_DEFAULT_OPTIONS)

    def __str__(self):
        """
        String representation of SlickSlider class.
        """
        return "Slick Slider: {title}".format(title=self.title)


@python_2_unicode_compatible
class SlickSliderImage(CMSPlugin):
    """
    Image model für SlickSlider class.
    """
    image = FilerImageField(
        verbose_name=_('Slider Image'),
        related_name='slider_images_filer')

    link = models.URLField(
        verbose_name=_('Image link'),
        null=True, blank=True)

    def __str__(self):
        """
        String representation of SlickSliderImage class.
        """
        return "Slick Slider Image: {filename}".format(
            filename=self.image.name)

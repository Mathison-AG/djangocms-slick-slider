#!/usr/bin/env python
# -*- coding: utf-8 -*-
import factory

from djangocms_slick_slider import models


class SliderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SlickSlider

    title = 'Test Slider'


class SliderImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SlickSliderImage

    caption_text = 'Test Caption'

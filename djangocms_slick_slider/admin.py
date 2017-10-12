# -*- coding: utf-8 -*-
from django.db import models
from django.forms import Textarea

from .settings import SLICK_SLIDER_ACE_THEME, SLICK_SLIDER_ACE_MODE


class SlickerSliderAceMixin:
    change_form_template = 'djangocms_slick_slider/admin/change_form.html'
    text_area_attrs = {
        'rows': 20,
        'data-editor': True,
        'data-mode': SLICK_SLIDER_ACE_THEME,
        'data-theme': SLICK_SLIDER_ACE_MODE,
    }

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs=text_area_attrs)}
    }

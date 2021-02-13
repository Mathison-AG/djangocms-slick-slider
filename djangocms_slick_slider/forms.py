# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms

from .models import SlickSlider
from .settings import get_setting


class SlickSliderForm(forms.ModelForm):
    model = SlickSlider

    def __init__(self, *args, **kwargs):
        super(SlickSliderForm, self).__init__(*args, **kwargs)
        self.fields['settings'].initial = get_setting(
            'SLICK_SLICKER_DEFAULT_OPTIONS')

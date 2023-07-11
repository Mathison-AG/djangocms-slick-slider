from django.test import TestCase

from djangocms_slick_slider import settings
from djangocms_slick_slider import apps

from ._factories import SliderFactory


class SlickSliderModelTests(TestCase):
    def setUp(self):
        self.assertEqual(apps.DjangocmsSlickSliderConfig.name, "djangocms_slick_slider")

        self.slider = SliderFactory()

    def test_string_repr(self):
        self.assertEqual(str(self.slider), "Test Slider")

    def test_settings_default(self):
        self.assertEqual(self.slider.settings, settings.SLIDER_DEFAULT)

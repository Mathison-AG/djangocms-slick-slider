from django.test import TestCase
from django.test.client import RequestFactory

from app_helper.base_test import CreateTestDataMixin
from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from djangocms_slick_slider.cms_plugins import SlickSliderPlugin

from ._factories import SliderFactory, SliderImageFactory


class SlickSliderPluginTests(CreateTestDataMixin, TestCase):
    def create_images(self, slider):
        for n in range(1, 7):
            image = self.create_filer_image_object()
            slider_image = SliderImageFactory.create(
                id=n, image=image, slider_id=slider.id
            )
            self.assertEqual(str(slider_image), "test_file.jpg")

    def setUp(self):
        self.slider = SliderFactory.create()
        self.create_images(self.slider)

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot="test")

        model_instance = add_plugin(placeholder, SlickSliderPlugin, "de")
        model_instance.copy_relations(self.slider)
        renderer = ContentRenderer(request=RequestFactory())
        from sekizai.context import SekizaiContext

        html = renderer.render_plugin(model_instance, SekizaiContext())
        self.assertIn('class="slider-wrapper"', html)
        self.assertIn('id="slider-%s' % model_instance.id, html)

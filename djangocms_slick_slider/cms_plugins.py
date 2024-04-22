import django
from django.contrib import admin

if django.VERSION >= (4, 0):
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .admin import SlickerSliderAceMixin
from .forms import SlickSliderForm
from .helpers import get_slider_image_dimensions
from .models import SlickSlider, SlickSliderImage


class SlickSliderImageInline(admin.TabularInline):
    model = SlickSliderImage
    extra = 1


@plugin_pool.register_plugin
class SlickSliderPlugin(SlickerSliderAceMixin, CMSPluginBase):
    """
    The main Slick Slider Plugin. Here, we can define various settings
    and behavior of the plugin.

    This Plugin adds a Slick Slider Plugin to Django CMS. You can add
    images as inline objects. The images will be rendered as thumbnails.


    You can define `SLICK_SLIDER_CONTAINER_WIDTH` to change the behaviors.
    Check :class:`helpers.get_slider_image_dimensions` for more information.
    """

    model = SlickSlider
    form = SlickSliderForm
    name = _("Slick Slider")
    render_template = "djangocms_slick_slider/base.html"
    cache = False
    inlines = [
        SlickSliderImageInline,
    ]

    def render(self, context, instance, placeholder):
        context = super(
            SlickSliderPlugin,
            self,
        ).render(context, instance, placeholder)

        # define context vars
        images = instance.images.all()

        if instance.settings:
            no_of_images = instance.settings.get("slidesToShow", 4)
        else:
            no_of_images = 4

        child_width = get_slider_image_dimensions(no_of_images)

        context.update({"images": images, "child_width": child_width})
        return context

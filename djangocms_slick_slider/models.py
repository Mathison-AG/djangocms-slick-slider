from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from jsonfield import JSONField


class SlickSlider(CMSPlugin):
    """
    Main Plugin Model for the slider.
    """
    class Meta:
        verbose_name = _('slick slider')
        verbose_name_plural = _('slick sliders')

    title = models.CharField(
        verbose_name=_('slider title'),
        max_length=255,
        null=True,
        blank=True,
    )

    settings = JSONField(
        verbose_name=_('slick settings'),
        blank=True,
        null=True,
        help_text=_('Check <a href="http://kenwheeler.github.io/slick/" '
                    'target="_blank">'
                    'Slick Documentation</a> for possible settings '
                    '<br>'
                    'Use JSON format and check the errors in the editor<br>'
                    'You can also use online JSON validators'))

    arrow_color = models.CharField(
        verbose_name=_('arrow color'),
        max_length=255,
        default="#666",
        help_text=_('Define the color of slider arrows here. All CSS '
                    'color values work (e.g. #efefef).'),
    )

    full_width = models.BooleanField(
        verbose_name=_('full width'),
        default=False,
    )

    slider_max_height = models.IntegerField(
        verbose_name=_('max. height'),
        blank=True,
        null=True,
        help_text=_('Define max height of the slider.'),
    )

    image_max_width = models.IntegerField(
        verbose_name=_('max. width'),
        blank=True,
        null=True,
        help_text=_('Define max height of the slider.'),
    )

    lazy_load_images = models.BooleanField(
        verbose_name=_('lazy load images'),
        help_text=_('Set to true if images should load lazily.'),
        default=True,
    )

    def copy_relations(self, oldinstance):
        """
        Take an instance and copy the images of that instance to this
        instance.
        """
        for image in oldinstance.images.all():
            image.pk = None
            image.slider = self
            image.save()

    def __str__(self):
        """
        String representation of SlickSlider class.
        """
        return "{title}".format(title=self.title)


class SlickSliderImage(models.Model):
    """
    Image model für SlickSlider class.
    """
    class Meta:
        verbose_name = _('slider image')
        verbose_name_plural = _('slider images')
        ordering = ['position']

    slider = models.ForeignKey(
        SlickSlider,
        related_name="images",
        on_delete=models.CASCADE,
    )

    image = FilerImageField(
        verbose_name=_('slider Image'),
        related_name='slider_images_filer',
        on_delete=models.CASCADE,
    )

    link = models.URLField(
        verbose_name=_('image link'),
        null=True,
        blank=True,
    )

    link_target = models.BooleanField(
        verbose_name=_('image link target'),
        help_text=_('open link in new window'),
        default=True,
    )

    caption_text = models.TextField(
        _('caption text'),
        null=True,
        blank=True,
    )

    position = models.IntegerField(
        _('position'),
        default=100,
    )

    def __str__(self):
        """
        String representation of SlickSliderImage class.
        """
        return "{filename}".format(filename=self.image.original_filename)

    def full_width_dimensions(self):
        """
        Return the thumbnail dimensions based on Slider full width settings.
        """
        if self.slider.full_width:
            return "%sx%s" % (
                self.slider.image_max_width,
                self.slider.slider_max_height,
            )
        return "1200x500"

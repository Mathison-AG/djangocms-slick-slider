from django.conf import settings


SLICK_SLIDER_VERSION = getattr(settings, 'SLICK_SLIDER_VERSION', '1.8.0')

SLICK_SLICKER_DEFAULT_OPTIONS = ('''
{
  "dots":true,
  "slidesToShow":4,
  "mobileFirst":true,
  "slidesToScroll":4
}
''')

SLICK_SLIDER_ACE_THEME = getattr(settings, 'SLICK_SLIDER_ACE_THEME', 'json')
SLICK_SLIDER_ACE_MODE = getattr(settings, 'SLICK_SLIDER_ACE_MODE', 'github')

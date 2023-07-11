from django.conf.urls import include, url

from djangocms_slick_slider.urls import urlpatterns as djangocms_slick_slider_urls

urlpatterns = [
    url(r"^", include(djangocms_slick_slider_urls, namespace="djangocms_slick_slider")),
]

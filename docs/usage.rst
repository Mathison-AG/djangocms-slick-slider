=====
Usage
=====

To use djangocms_slick_slider in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'djangocms_slick_slider.apps.DjangocmsSlickSliderConfig',
        ...
    )

Add djangocms_slick_slider's URL patterns:

.. code-block:: python

    from djangocms_slick_slider import urls as djangocms_slick_slider_urls


    urlpatterns = [
        ...
        url(r'^', include(djangocms_slick_slider_urls)),
        ...
    ]

=============================
djangocms_slick_slider
=============================

.. image:: https://badge.fury.io/py/djangocms-slick-slider.svg
    :target: https://badge.fury.io/py/djangocms-slick-slider

.. image:: https://travis-ci.org/oesah/djangocms-slick-slider.svg?branch=master
    :target: https://travis-ci.org/oesah/djangocms-slick-slider

.. image:: https://codecov.io/gh/oesah/djangocms-slick-slider/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/oesah/djangocms-slick-slider

A Django CMS Slider Plugin with Slick

Documentation
-------------

The full documentation is at https://djangocms-slick-slider.readthedocs.io.

Quickstart
----------

Install djangocms_slick_slider::

    pip install djangocms-slick-slider

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

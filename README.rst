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


Settings
--------

``SLICK_SLIDER_VERSION``

Version of Slick Slider that should be used. Keep in mind, that this version
needs to be in `static/vendor/` folder with the appropriate folder name.

If you want to upgrade, download and copy the new version into the before
mentioned folder and change the version in the settings.

default: ``1.8.0``


Features
--------

* Add a Slick Slider to any page via Django CMS Plugin

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

If you have issues with different python versions, please take a look at
these docs: https://www.holger-peters.de/using-pyenv-and-tox.html

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

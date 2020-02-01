from django.conf import settings
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = [
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': {
            'cmspages': CMSSitemap
        }},
    ),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        path('media/<path:path>', serve, {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
    ] + staticfiles_urlpatterns() + urlpatterns

from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
import ask.urls


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^', include(ask.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

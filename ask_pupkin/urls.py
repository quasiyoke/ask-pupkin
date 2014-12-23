from django.contrib import admin
from django.conf.urls import patterns, include, url
import ask.urls


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^', include(ask.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

import views
from django.contrib import admin
from django.conf.urls import patterns, include, url


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^helloworld\.wsgi$', views.Helloworld.as_view(), name='helloworld'),
)

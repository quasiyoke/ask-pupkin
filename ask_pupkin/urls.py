import views
from django.contrib import admin
from django.conf.urls import patterns, include, url


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^helloworld\.wsgi$', views.Helloworld.as_view(), name='helloworld'),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^login/$', views.Login.as_view(), name='login'),
)

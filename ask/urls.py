import views
from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^helloworld\.wsgi$', views.Helloworld.as_view(), name='helloworld'),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^questions/(?P<pk>\d+)/$', views.Question.as_view(), name='question'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^login/$', views.Login.as_view(), name='login'),
)

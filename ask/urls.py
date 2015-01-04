import views
from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^helloworld\.wsgi$', views.Helloworld.as_view(), name='helloworld'),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^profiles/(?P<pk>\d+)/$', views.Profile.as_view(), name='profile'),
    url(r'^questions/$', views.Questions.as_view(), name='questions'),
    url(r'^questions/(?P<pk>\d+)/$', views.Question.as_view(), name='question'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
)

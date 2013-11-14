#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'mv_test.views.index', name='mv_test'),
    url(r'^(?P<gid>\d+)/$', 'mv_test.views.group', name='mv_test-group'),
)

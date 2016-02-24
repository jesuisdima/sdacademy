from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
url(r'^$', views.list_view, name="students"),
url(r'^(?P<id>\d+)/$', views.detail, name="students"),
)
from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
url(r'^$', views.course_list_index, name="index"),
url(r'^(?P<id>\d+)/$', views.detail, name='courses'),
)
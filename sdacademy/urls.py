from django.conf.urls import patterns, include, url
from django.contrib import admin

from sdacademy.views import index, contact, student_list, student_detail
from courses.views import course_list_index

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^$', course_list_index, name="index"),
    url(r'^index/', course_list_index, name="index"),
    #url(r'^$', include('courses.urls', namespace='courses')),
    #url(r'^index/', include('courses.urls', namespace='courses')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^contact/', contact, name="contact"),
    url(r'^student_list/', student_list, name="student_list"),
    url(r'^student_detail/', student_detail, name="student_detail"),
)

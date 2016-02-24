# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from courses.models import Course, Lesson



def course_list_index(request):
	course_list = Course.objects.all()
	template = loader.get_template('courses/index.html')
	context = RequestContext(request, {
        'course_list': course_list,
        })
	return HttpResponse(template.render(context))

def detail(request, id):
	course_details = Course.objects.get(id=id)
	lesson_list = Lesson.objects.filter(course=id)
	template = loader.get_template('courses/detail.html')
	context = RequestContext(request, {
        'course_details': course_details,
        'lesson_list': lesson_list
        })
	return HttpResponse(template.render(context))

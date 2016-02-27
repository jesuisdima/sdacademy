# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from courses.models import Course
from coaches.models import Coach


def detail(request, id):
	coach_details = Coach.objects.get(id=id)
	course_list_coach = Course.objects.filter(coach=id)
	course_list_assistant = Course.objects.filter(assistant=id)
	template = loader.get_template('coaches/detail.html')
	context = RequestContext(request, {
        'coach_details': coach_details,
        'course_list_coach': course_list_coach,
        'course_list_assistant': course_list_assistant
        })
	return HttpResponse(template.render(context))


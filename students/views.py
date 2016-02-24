# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from students.models import Student
from courses.models import Course



def list_view(request):
	course_id = request.GET.get('course_id','')

	try:
		course_id = int(course_id)
	except:
		pass

	if course_id:
		student_list = Student.objects.filter(courses=course_id)
	else:
		student_list = Student.objects.all()

	template = loader.get_template('students/list.html')
	context = RequestContext(request, {
        'student_list': student_list
        })
	return HttpResponse(template.render(context))


def detail(request, id):
	students_details = Student.objects.get(id=id)
	course_list = Course.objects.filter(student=id)
	template = loader.get_template('students/detail.html')
	context = RequestContext(request, {
        'students_details': students_details,
        'course_list': course_list
        })
	return HttpResponse(template.render(context))
	
# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm



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


def detail(request, pk):
	students_details = Student.objects.get(id=pk)
	course_list = Course.objects.filter(student=pk)
	template = loader.get_template('students/detail.html')
	context = RequestContext(request, {
        'students_details': students_details,
        'course_list': course_list
        })
	return HttpResponse(template.render(context))

def create(request):
	if request.method == "POST":
		model_form = StudentModelForm(request.POST)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 
				'Student %s %s has been successfully added.' % (application.name, application.surname))
			return redirect('students:list_view')
	else:
		model_form = StudentModelForm()
	template = loader.get_template('students/add.html')
	context = RequestContext(request, {
    'model_form': model_form,
        })
	return HttpResponse(template.render(context))


def edit(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == "POST":
		model_form = StudentModelForm(request.POST, instance=application)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 
				'Info on the student has been sucessfully changed.')
			return redirect('students:edit', application.id)
	else:
		model_form = StudentModelForm(instance=application)
	template = loader.get_template('students/edit.html')
	context = RequestContext(request, {
    'model_form': model_form,
        })
	return HttpResponse(template.render(context))

def remove(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == "POST":
		application.delete()
		messages.success(request, 
				'Info on %s %s has been sucessfully deleted.' % (application.name, application.surname))
		return redirect('students:list_view')
	template = loader.get_template('students/remove.html')
	context = RequestContext(request, {
    'model_info': application,
        })
	return HttpResponse(template.render(context))

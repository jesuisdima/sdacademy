# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages

from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm



def course_list_index(request):
	course_list = Course.objects.all()
	template = loader.get_template('index.html')
	context = RequestContext(request, {
        'course_list': course_list,
        })
	return HttpResponse(template.render(context))

def detail(request, pk):
	course_details = Course.objects.get(id=pk)
	lesson_list = Lesson.objects.filter(course=pk)
	coach_list = Coach.objects.filter(coach_courses=pk)
	template = loader.get_template('courses/detail.html')
	context = RequestContext(request, {
        'course_details': course_details,
        'lesson_list': lesson_list,
        'coach_list': coach_list
        })
	return HttpResponse(template.render(context))


def add(request):
	if request.method == "POST":
		model_form = CourseModelForm(request.POST)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 
				'Course %s has been successfully added.' % application.name)
			return redirect('index')
	else:
		model_form = CourseModelForm()
	template = loader.get_template('courses/add.html')
	context = RequestContext(request, {
    'model_form': model_form,
        })
	return HttpResponse(template.render(context))
	

def edit(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == "POST":
		model_form = CourseModelForm(request.POST, instance=application)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 
				'The changes have been saved.')
			return redirect('courses:edit', application.id)
	else:
		model_form = CourseModelForm(instance=application)
	template = loader.get_template('courses/edit.html')
	context = RequestContext(request, {
    'model_form': model_form,
        })
	return HttpResponse(template.render(context))



def remove(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == "POST":
		application.delete()
		messages.success(request, 
				'Course %s has been deleted.' % application.name)
		return redirect('index')
	template = loader.get_template('courses/remove.html')
	context = RequestContext(request, {
    'model_info': application,
        })
	return HttpResponse(template.render(context))


def add_lesson(request, pk):
	if request.method == "POST":
		model_form = LessonModelForm(request.POST)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 
				'Lesson %s has been successfully added.' % application.subject)
			return redirect('index')
	else:
		application_course = Course.objects.get(id=pk)
		model_form = LessonModelForm(initial={'course':application_course})
	template = loader.get_template('courses/add_lesson.html')
	context = RequestContext(request, {
    'model_form': model_form,
        })
	return HttpResponse(template.render(context))


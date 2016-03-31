# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/detail.html'
	context_object_name = 'course_details'

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		context['lesson_list'] = Lesson.objects.filter(course=self.kwargs['pk'])
		context['coach_list'] = Coach.objects.filter(coach_courses=self.kwargs['pk'])
		return context


class CourseCreateView(CreateView):
	model = Course
	success_url = reverse_lazy('index')
	template_name = 'courses/add.html'

	def get_context_data(self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = "Course creation"
		context['page_title'] = "SD Academy - Add course"
		return context

	def form_valid(self, form):
		instance = form.save(commit=False)
		messages.success(self.request, 
				'Course %s has been successfully added.' % instance.name)
		return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'courses/edit.html'

	def get_context_data(self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Course update"
		context['page_title'] = "SD Academy - Edit course"
		return context

	def get_success_url(self):
		return reverse('courses:edit', kwargs={
			'pk': self.object.pk,
			})

	def form_valid(self, form):
		messages.success(self.request, 
				'The changes have been saved.')
		return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'courses/remove.html'
	context_object_name = 'model_info'
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Course deletion"
		return context

	def delete(self, request, **kwargs):
		instance = Course.objects.get(id=self.kwargs['pk'])
		messages.success(self.request, 'Course %s has been deleted.' % instance.name)
		return super(CourseDeleteView, self).delete(request, **kwargs)


def add_lesson(request, pk):
	application_course = Course.objects.get(id=pk)
	if request.method == "POST":
		model_form = LessonModelForm(request.POST)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 
				'Lesson %s has been successfully added.' % application.subject)
			return redirect('courses:detail', application_course.id)
	else:
		model_form = LessonModelForm(initial={'course':application_course})
	template = loader.get_template('courses/add_lesson.html')
	context = RequestContext(request, {
    'model_form': model_form,
        })
	return HttpResponse(template.render(context))


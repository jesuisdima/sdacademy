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

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm



class StudentListView(ListView):
	model = Student
	paginate_by = 2

	def get_queryset(self):
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			students = Student.objects.filter(courses=course_id)
		else:
			students = Student.objects.all()
		return students


class StudentDetailView(DetailView):
	model = Student

	def get_context_data(self, **kwargs):
		context = super(StudentDetailView, self).get_context_data(**kwargs)
		context['course_list'] = Course.objects.filter(student=self.kwargs['pk'])
		return context


class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	
	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = "Student registration"
		context['page_title'] = "SD Academy - Add student"
		return context

	def form_valid(self, form):
		instance = form.save(commit=False)
		messages.success(self.request, 
				'Student %s %s has been successfully added.' % (instance.name, instance.surname))
		return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
	model = Student

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Student info update"
		context['page_title'] = "SD Academy - Edit student"
		return context

	def get_success_url(self):
		return reverse('students:edit', kwargs={
			'pk': self.object.pk,
			})

	def form_valid(self, form):
		messages.success(self.request, 
				'Info on the student has been sucessfully changed.')
		return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
		return context

	def delete(self, request, **kwargs):
		instance = Student.objects.get(id=self.kwargs['pk'])
		messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (instance.name, instance.surname))
		return super(StudentDeleteView, self).delete(request, **kwargs)


# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm



class StudentListView(ListView):
	model = Student
	template_name = "students/list.html"
	context_object_name = "student_list"

	def get_queryset(self):
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			students = Student.objects.filter(courses=course_id)
		else:
			students = Student.objects.all()
		return students


class StudentDetailView(DetailView):
	model = Student
	template_name = "students/detail.html"
	context_object_name = "students_details"

	def get_context_data(self, **kwargs):
		context = super(StudentDetailView, self).get_context_data(**kwargs)
		context['course_list'] = Course.objects.filter(student=self.kwargs['pk'])
		return context


class StudentCreateView(CreateView):
	model = Student
	template_name = "students/add.html"
	success_url = reverse_lazy('students:list_view')
	
	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = "Student registration"
		return context

	def form_valid(self, form):
		instance = form.save(commit=False)
		messages.success(self.request, 
				'Student %s %s has been successfully added.' % (instance.name, instance.surname))
		return super(StudentCreateView, self).form_valid(form)


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

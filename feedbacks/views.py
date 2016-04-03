# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail, mail_admins

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from feedbacks.models import Feedback


class FeedbackView(CreateView):
	model = Feedback
	success_url = reverse_lazy('feedback')
	template_name = 'feedback.html'

	def get_context_data(self, **kwargs):
		context = super(FeedbackView, self).get_context_data(**kwargs)
		context['title'] = "Leave your feedback"
		return context

	def form_valid(self, form):
		data = form.cleaned_data
		mail_admins(data['subject'], data['message'], fail_silently=False)
		messages.success(self.request, 
				'Thank you for your feedback! We will keep in touch with you very soon!')
		return super(FeedbackView, self).form_valid(form)

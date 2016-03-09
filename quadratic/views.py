# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from forms import messages, QuadraticForm
from django import forms


def quadratic_results(request):
	discrim = None
	final_message = None
	if request.method == "GET" and len(request.GET):
		form = QuadraticForm(request.GET)
		if form.is_valid():
			if form.clean_a():
				a = int(request.GET['a'])
				b = int(request.GET['b'])
				c = int(request.GET['c'])
				discrim = b**2 - 4 * a * c
				if discrim < 0:
					final_message = messages['mes5']
				if discrim == 0:
					x1 = -b/2*a
					final_message = ''.join(messages['mes6'] + str(round(float(x1), 1)))
				if discrim > 0:
					x1 = (-b+discrim**0.5)/(2*a)
					x2 = (-b-discrim**0.5)/(2*a)
					final_message = ''.join(messages['mes4'] + 
					'x1 = ' + str(round(float(x1), 1)) + ', x2 = ' + str(round(float(x2), 1)))
				discrim = int(discrim)
	else:
		form = QuadraticForm()
	return render(request, 'quadratic/results.html', {
		'discrim':discrim, 
		'final_message':final_message,
		'form':form})

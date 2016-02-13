# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def quadratic_results(request):
	a = request.GET['a']
	if int(a):
		a = int(a)
	else:
		a = "коэффициент не целое число"
	return render(request, 'results.html')


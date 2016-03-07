# -*- coding: UTF-8 -*-

from django import forms

class QuadraticForm(forms.Form):
	a = forms.FloatField(label="коэффициент a")
	b = forms.FloatField(label="коэффициент b")
	c = forms.FloatField(label="коэффициент c")

def clean_a(request):
	if request.method == "GET":
		form = QuadraticForm(request.GET)
		if form.is_valid():
			print "form is valid"
	else:
		form = QuadraticForm()
	return form
	#return render(request, 'quadratic/results.html',{'form': None})

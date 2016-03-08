# -*- coding: UTF-8 -*-

from django import forms

messages = {
	'mes1': 'коэффициент не определен',
	'mes2': 'коэффициент не целое число',
	'mes3': 'коэффициент при первом слагаемом уравнения не может быть равным нулю',
	'mes4': 'Квадратное уравнение имеет два действительных корня: ',
	'mes5': 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.',
	'mes6': 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = '
}

class QuadraticForm(forms.Form):
	a = forms.FloatField(label="коэффициент a")
	b = forms.FloatField(label="коэффициент b")
	c = forms.FloatField(label="коэффициент c")


	def clean_a(self):
		data = self.cleaned_data['a']
		if data == float(0):
			raise forms.ValidationError(messages['mes3'])
		return data

# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

messages = {
	'mes1': 'коэффициент не определен',
	'mes2': 'коэффициент не целое число',
	'mes3': 'коэффициент при первом слагаемом уравнения не может быть равным нулю',
	'mes4': 'Квадратное уравнение имеет два действительных корня: ',
	'mes5': 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.',
	'mes6': 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = '
}

def quadratic_results(request):

	a = request.GET.get('a','')
	b = request.GET.get('b','')
	c = request.GET.get('c','')
	
	values = [a,b,c]
	value_comment = ['','','']

	for i in range(len(values)):
		try:
			values[i] = int(values[i])
			value_comment[i] = ''
		except:
			if len(values[i]) == 0:
				value_comment[i] = messages['mes1']
			else:
				value_comment[i] = messages['mes2']

	try:
		a = int(a)
		b = int(b)
		c = int(c)
	except:
		pass

	try:
		value_comment[0] = messages['mes3'] if int(a) == 0 else value_comment[0]
	except:
		pass

	x1 = float()
	x2 = float()

	try:
		discrim = b**2 - 4 * a * c
		if discrim < 0:
			final_message = messages['mes5']
		if discrim == 0:
			x1 = -b/2*a
			final_message = ''.join(messages['mes6'] + str(float(x1)))
		if discrim > 0:
			x1 = (-b+discrim**0.5)/(2*a)
			x2 = (-b-discrim**0.5)/(2*a)
			final_message = ''.join(messages['mes4'] + 
				'x1 = ' + str(float(x1)) + ', x2 = ' + str(float(x2)))
	except:
		discrim = ''
		final_message = ''

	return render(request, 'results.html', {
		'a':a, 'a_comment':value_comment[0],
		'b':b, 'b_comment':value_comment[1],
		'c':c, 'c_comment':value_comment[2],
		'discrim':discrim, 
		'final_message':final_message})

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

	values = [request.GET['a'], request.GET['b'], request.GET['c']]
	for i in range(len(values)):
		try:
			values[i] = int(values[i])
		except:
			if len(values[i]) == 0:
				values[i] = messages['mes1']
			else:
				values[i] = messages['mes2']

	a = values[0]
	b = values[1]
	c = values[2]

	a = messages['mes3'] if a == 0 else a

	x1 = ''
	x2 = ''
	try:
		discrim = b**2 - 4 * a * c
		if discrim < 0:
			final_message = messages['mes5']
		if discrim == 0:
			x1 = -b/2*a
			final_message = ''.join(messages['mes6'] + str(round(x1,3)))
		if discrim > 0:
			x1 = (-b+discrim**0.5)/(2*a)
			x2 = (-b-discrim**0.5)/(2*a)
			final_message = ''.join(messages['mes4'] + 
				'x1 = ' + str(round(x1,3)) + ', x2 = ' + str(round(x2,3)))
	except:
		discrim = ''
		final_message = ''


	return render(request, 'results.html', {
		'a':a, 
		'b':b, 
		'c':c,
		'discrim':discrim, 
		'final_message':final_message})

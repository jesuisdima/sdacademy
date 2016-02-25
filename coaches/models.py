# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
	user = models.OneToOneField(User)
	date_of_birth = models.DateField(help_text="дата рождения")
	gender = models.CharField(max_length=1,
		choices=(('M', 'Male'), ('F', 'Female')),
		help_text="пол")
	phone = models.CharField(max_length=32, help_text="телефон")
	address = models.CharField(max_length=255, help_text="адрес")
	skype = models.CharField(max_length=32)
	description = models.TextField(help_text="описание")

	#def __unicode__(self):
		#return self.name
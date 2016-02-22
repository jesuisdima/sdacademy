# -*- coding: UTF-8 -*-
from django.db import models
from courses.models import Course

class Student(models.Model):
	name = models.CharField(max_length=32, help_text="имя")
	surname = models.CharField(max_length=64, help_text="фамилия")
	date_of_birth = models.DateField(help_text="дата рождения")
	email = models.EmailField()
	phone = models.CharField(max_length=32, help_text="телефон")
	address = models.CharField(max_length=255, help_text="адрес")
	skype = models.CharField(max_length=32)
	courses = models.ManyToManyField(Course, help_text="курсы, на которых учится студент")

	def __unicode__(self):
		return self.name
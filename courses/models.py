# -*- coding: UTF-8 -*-
from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=64, help_text="название")
	short_description = models.CharField(max_length=128, help_text="краткое описание")
	description = models.TextField(help_text="полное описание")

	def __unicode__(self):
		return self.name

class Lesson(models.Model):
	subject = models.CharField(max_length=128, help_text="тема")
	description = models.TextField(help_text="описание")
	course = models.ForeignKey(Course, help_text="курс")
	order = models.PositiveIntegerField(help_text="номер по порядку")

	def __unicode__(self):
		return self.subject

# -*- coding: UTF-8 -*-

from django.db import models

class Feedback(models.Model):
	name = models.CharField(max_length=32, help_text="имя отправителя")
	subject = models.CharField(max_length=128, help_text="тема сообщения")
	message = models.TextField(help_text="сообщение")
	from_email = models.EmailField(help_text="email отправителя")
	create_date = models.DateTimeField(auto_now_add=True, help_text="дата и время обращения")

	def __unicode__(self):
		return self.name

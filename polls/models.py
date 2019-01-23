# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from datetime import timedelta, datetime
from django.utils.timezone import make_aware

@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text= models.CharField(max_length=200)
	votes= models.IntegerField(default=0)

	def __str__(self):
			return self.choice_text

class Forecast(models.Model):

	timestamp = models.DateTimeField()
	temperature = models.DecimalField(max_digits=12, decimal_places=2)
	description = models.CharField(max_length=150)
	city = models.CharField(max_length=150)
	humidity = models.DecimalField(max_digits=12,decimal_places=2, default=0)

	def __str__(self):

		return str(self.timestamp)

	def save(self, *args, **kwargs):
		if not self.id:
			naive_datetime = datetime.now()
			aware_datetime = make_aware(naive_datetime)
			#self.timestamp = aware_datetime
			self.timestamp = timezone.now()
		return super(Forecast, self).save(*args, **kwargs)

#make schedule model.
#name
#Start time
#duration
#day of week
#jobid

# class Schedule(models.Model):

# 	name = models.CharField(max_length=150)
# 	start_time = models.TimeField()
# 	duration = models.IntegerField(default=0)
# 	day_of_week = models.IntegerField(default=0)

# 	def save(self,
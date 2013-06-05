# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Sticker(models.Model):
	name = models.CharField(max_length=200)
	size = models.CharField(max_length=20,null=True)
	image_path = models.CharField(max_length=1000,null=True)
	description = models.CharField(max_length=1000,default=' ',null=True)

	def __unicode__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200,default=' ',null=True)

	def __unicode__(self):
		return self.name

class Order(models.Model):
	date_time = models.DateTimeField('Order date and time')
	user = models.ForeignKey(User)
	def __unicode__(self):
		return str(self.date_time)

class OrderItem(models.Model):
	sticker = models.ForeignKey(Sticker)
	quantity = models.IntegerField(default=0)
	order = models.ForeignKey(Order)
	
	def create_order_item(self,sticker_id,order_id,quantity):
		self.sticker = sticker_id
		self.quantity = quantity
	def __unicode__(self):
		return str(self.sticker)+' '+str(self.quantity)
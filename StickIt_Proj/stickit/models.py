# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200,default=' ',null=True)

	def __unicode__(self):
		return self.name

class Size(models.Model):
	name = models.CharField(max_length=70)
	description = models.CharField(max_length=200,default=' ',null=True)
	width = models.IntegerField(default=200, null=True)
	height = models.IntegerField(default=150, null=True)

	def __unicode__(self):
		return self.name+' ('+str(self.width)+'x'+str(self.height)+')'

class Sticker(models.Model):
	name = models.CharField(max_length=200)
	size = models.ForeignKey(Size,null=True)
	image_path = models.CharField(max_length=1000,null=True)
	description = models.CharField(max_length=1000,default=' ',null=True)
	subject = models.ManyToManyField(Subject, null=True)
	price = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	def __unicode__(self):
		return self.name

class Order(models.Model):
	date_time = models.DateTimeField('Order date and time')
	user = models.ForeignKey(User)
	processed = models.IntegerField(default=0)
	def __unicode__(self):
		return str(self.date_time)

class OrderItem(models.Model):
	sticker = models.ForeignKey(Sticker)
	quantity = models.IntegerField(default=0)
	order = models.ForeignKey(Order)
	
	def create_order_item(sticker_id,order_id,quantity):
		self.order = order_id
		self.sticker = sticker_id
		self.quantity = quantity
	def __unicode__(self):
		return str(self.sticker)+' '+str(self.quantity)
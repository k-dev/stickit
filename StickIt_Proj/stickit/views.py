# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from models import Subject, Sticker, Order, OrderItem
from django.contrib.auth.models import User
from django import forms
from django.utils.timezone import utc
import os, datetime

def index(request):
	# header_content = open('/Users/kirill/Web-Coding/stickit/StickIt_Proj/stickit/static/header/header_content.txt', 'r').read()
	return render(request, 'stickit/index.html')
	#return HttpResponse("The simplest view")

def info(request):
	# header_content = open('/Users/kirill/Web-Coding/stickit/StickIt_Proj/stickit/static/header/header_content.txt', 'r').read()
	return render(request, 'stickit/info.html')

def store(request, subject_id=0):
	subjects_list = Subject.objects.all()
	print(str(subject_id))
	if subject_id != 0:
		stickers_list = Sticker.objects.filter(subject=subject_id)
	else:
		stickers_list = Sticker.objects.all()
	subjects = Subject.objects.filter(pk=subject_id)
	subject_name = 'All'
	if len(subjects) > 0:
		subject_name = subjects[0].name
	context = { 'subjects_list' : subjects_list,
				'stickers_list' : stickers_list,
				'selected_subject' : subject_name, }
	return render(request, 'stickit/store.html', context)

def cart(request):
	return render(request, 'stickit/cart.html')

def checkout(request, step=0):
	if (request.method == 'POST'):
		if request.user.is_authenticated():
			now = datetime.datetime.utcnow().replace(tzinfo=utc)
			current_user = request.user
			current_order = Order(date_time=now,user=current_user)
			current_order.save()
			for i in range(1, 6):
				print(request.POST)
				try:
				    item_quantity = int(request.POST['item_quantity_'+str(i)])
				except:
				    item_quantity = None
				if not item_quantity is None:
					item_id = request.POST['item_options_'+str(i)].split(' ')[1]
					print(item_id)
					current_sticker = Sticker.objects.get(pk=int(item_id))
					print(current_sticker)
					order_item = OrderItem(order=current_order,sticker=current_sticker,quantity=item_quantity)
					order_item.save()
	return redirect('/order/'+str(current_order.id)+'/1')

def buy(request, item_id=0):
	if request.user.is_authenticated():
		print()
	else:
		return redirect('/login')
	return redirect('/cart')

def payment(request,order_id):
	if request.user.is_authenticated():
		order = get_object_or_404(Order,pk=order_id)
	else:
		return redirect('/login')
	context = {
		'user': request.user,
		'order': order, }
	return render(request, 'stickit/payment.html', context)

def orders(request):
	if request.user.is_authenticated():
		orders_list = Order.objects.filter(user=request.user)
		context = {
		'user': request.user,
		'orders_list': orders_list, }
	else:
		return redirect('/login')
	return render(request, 'stickit/orders.html', context)

def order(request,order_id,checkout=0):
	if request.user.is_authenticated():
		order = get_object_or_404(Order,pk=order_id)
		order_items = OrderItem.objects.filter(order=order_id)
	else:
		return redirect('/login')
	context = {
		'user': request.user,
		'order': order,
		'order_items': order_items,
		'checkout' : checkout }
	return render(request, 'stickit/order.html', context)

class UploadImageForm(forms.Form):
	image = forms.ImageField()

def save_file(file, path=''):
	filename = file._get_name()
	uploadsDir = os.path.dirname(os.path.dirname(__file__))+'/uploads'+str(path)
	if not os.path.exists(uploadsDir):
		os.makedirs(uploadsDir)
	fd = open('%s/%s' % (uploadsDir, str(filename)), 'wb')
	for chunk in file.chunks():
		fd.write(chunk)
	fd.close()

def order_custom(request):
	'''Simple view method for uploading an image
	'''
	if request.method == 'POST':
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid() and form.is_multipart():
			save_file(request.FILES['image'], '/images')
			return HttpResponse('Thanks for uploading the image')
		else:
			return HttpResponse('Invalid image')
	else:
		form = UploadImageForm()
	return render(request, 'stickit/order_custom.html', {'form': form})
	# return render(request, 'stickit/order_custom.html')

def contact(request):
	return render(request, 'stickit/contact.html')

def about(request):
	return render(request, 'stickit/about.html')

def sign_up(request):
	template = "stickit/sign_up.html"
	state = ""
	statecolor = "rgb(200, 100, 100)"
	username = password = password2 = email = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')
		email = request.POST.get('email')
		error = False
		if len(username) == 0:
			state = "Enter user name"
			error = True
		elif len(email) == 0:
			state = "Enter Email"
			error = True
		elif len(password) < 6:
			state = "Password must contain at least 6 characters."
			error = True
		elif not password == password2:
			state = "Passwords don't match"
			error = True
		elif User.objects.filter(username=username).count():
			state = "User already exists"
			error = True

		if not error:
			u = User(username=username,email=email)
			u.set_password(password)
			u.save()
			state="Registration succeed!"
			statecolor="rgb(100, 200, 100)"
			backenduser = authenticate(username=username, password=password)
			if backenduser is not None and backenduser.is_active:
				login(request, backenduser)
				template="stickit/index.html"
			username=''
			email=''

	context = { 'state' : state,
		   'statecolor' : statecolor,
		   'username' : username,
		   'email' : email }

	return render(request, template, context)

def login_user(request):
	state = ""
	username = password = ''
	print(request.REQUEST)
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You entered"
				return redirect('/')
			else:
				state = "Your account is disabled"
		else:
			state = "Wrong name or password"
	context = {
		'state': state,
		'user': request.user,}
	return render(request, 'stickit/login.html', context)

def logout_user(request):
	logout(request)
	return redirect('/')

def admin_cart(request):
	lastOrders = []
	for user in User.objects.all():
		orders = Order.objects.filter(user=user.id)
		if len(orders) > 0:
			lastOrder=orders[len(orders)-1]
			lastOrders.append(lastOrder)

	context = { 'users' : User.objects.all(),
			'orders' : lastOrders,
			'order_items' : OrderItem.objects.all(), }
	return render(request, 'stickit/admin_cart.html', context)

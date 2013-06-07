# coding: utf-8

from stickit.models import Sticker
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# header_content = open('/Users/kirill/Web-Coding/stickit/StickIt_Proj/stickit/static/header/header_content.txt', 'r').read()
	return render(request, 'stickit/index.html')
	#return HttpResponse("The simplest view")

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', 'stickit.views.index', name='index'),
	# url(r'^store', 'stickit.views.store'),
)
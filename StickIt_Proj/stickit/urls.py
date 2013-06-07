from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', 'stickit.views.index', name='index'),
	# url(r'^header/header_content.txt', TemplateView.as_view(template_name="{{STATIC_URL}}header/header_content.txt")),
)
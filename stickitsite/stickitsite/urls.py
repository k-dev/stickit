# coding: utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()   #функция автоматического обнаружения файлов admin.py в наших приложениях

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)), #URL админки http://stickit.com/admin/

    # Examples:
    # url(r'^$', 'stickitsite.views.home', name='home'),
    # url(r'^stickitsite/', include('stickitsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
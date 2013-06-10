# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()   #функция автоматического обнаружения файлов admin.py в наших приложениях

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/cart', 'stickit.views.admin_cart'),
	url(r'^$', include('stickit.urls')),
	# url(r'^stickit/', include('stickit.urls')),
	# url(r'^$', 'stickit.views.index'),
	url(r'^store/$', 'stickit.views.store'),
	url(r'^store/(?P<subject_id>\d+)', 'stickit.views.store'),
	url(r'^order_custom', 'stickit.views.order_custom'),
	url(r'^contact', 'stickit.views.contact'),
	url(r'^about', 'stickit.views.about'),
	url(r'^sign_up/$', 'stickit.views.sign_up'),
	url(r'^login/$', 'stickit.views.login_user'),
    url(r'^logout/$', 'stickit.views.logout_user'),
    url(r'^cart', 'stickit.views.cart'),
    url(r'^buy/(?P<item_id>\d+)/$', 'stickit.views.buy'),
    url(r'^order/(?P<order_id>\d+)/$', 'stickit.views.order'),
    url(r'^order/(?P<order_id>\d+)/(?P<checkout>\d+)$', 'stickit.views.order'),
    url(r'^orders', 'stickit.views.orders'),
    url(r'^checkout', 'stickit.views.checkout'),
    url(r'^checkout/(?P<step>\d+)/$', 'stickit.views.checkout'),
    url(r'^payment/(?P<order_id>\d+)/$', 'stickit.views.payment'),
    url(r'^info', 'stickit.views.info'),


    # Examples:
    # url(r'^$', 'stickitsite.views.home', name='home'),
    # url(r'^stickitsite/', include('stickitsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
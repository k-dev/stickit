from django.contrib import admin
from stickit.models import Subject, Size, Sticker, OrderItem, Order

admin.site.register(Subject)
admin.site.register(Size)
admin.site.register(Sticker)
admin.site.register(OrderItem)
admin.site.register(Order)
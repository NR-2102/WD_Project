from django.contrib import admin
from .models import Category, Products, Profile, Order, OrderItem
# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)

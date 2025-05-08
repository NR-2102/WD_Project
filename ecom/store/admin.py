from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Products, Profile, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'subtotal')
    can_delete = False

    def subtotal(self, obj):
        return obj.subtotal
    subtotal.short_description = 'Subtotal'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'order_date', 'status', 'colored_status', 'total_amount')
    list_filter = ('status', 'order_date')
    search_fields = ('order_number', 'user__username', 'user__email')
    readonly_fields = ('order_number', 'order_date', 'total_amount')
    inlines = [OrderItemInline]
    list_editable = ('status',)
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'order_date', 'status', 'total_amount')
        }),
        ('Shipping Information', {
            'fields': ('shipping_address', 'phone_number', 'email')
        }),
    )

    def colored_status(self, obj):
        colors = {
            'Pending': '#FFA500',  # Orange
            'Processing': '#1E90FF',  # Blue
            'Shipped': '#4169E1',  # Royal Blue
            'Delivered': '#32CD32',  # Green
            'Cancelled': '#FF0000',  # Red
        }
        color = colors.get(obj.status, '#808080')  # Default gray if status not found
        return format_html(
            '<span style="color: white; background-color: {}; padding: 5px 10px; border-radius: 4px;">{}</span>',
            color,
            obj.status
        )
    colored_status.short_description = 'Status Display'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'subtotal')
    list_filter = ('order__status',)
    search_fields = ('order__order_number', 'product__name')
    readonly_fields = ('order', 'product', 'quantity', 'price')

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Profile)


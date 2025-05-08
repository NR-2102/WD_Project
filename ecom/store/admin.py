from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Products, Profile, Order, OrderItem

# Inline admin for OrderItem to be displayed within the Order admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem  # Model for the inline display
    extra = 0  # No extra empty rows
    readonly_fields = ('product', 'quantity', 'price', 'subtotal')  # Fields displayed as readonly
    can_delete = False  # Disable deletion of order items from the inline

    # Custom method to display the subtotal of each order item
    def subtotal(self, obj):
        return obj.subtotal
    subtotal.short_description = 'Subtotal'  # Display name for the subtotal column

# Admin configuration for the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'order_date', 'status', 'colored_status', 'total_amount')  # Fields to display in the list view
    list_filter = ('status', 'order_date')  # Filters available in the sidebar
    search_fields = ('order_number', 'user__username', 'user__email')  # Fields to search by in the admin panel
    readonly_fields = ('order_number', 'order_date', 'total_amount')  # Read-only fields that cannot be edited
    inlines = [OrderItemInline]  # Inline the OrderItem model within the Order admin view
    list_editable = ('status',)  # Allows direct editing of the status field in the list view
    fieldsets = (  # Grouping fields into sections
        ('Order Information', {
            'fields': ('order_number', 'user', 'order_date', 'status', 'total_amount')
        }),
        ('Shipping Information', {
            'fields': ('shipping_address', 'phone_number', 'email')
        }),
    )

    # Custom method to display status with a color background
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
    colored_status.short_description = 'Status Display'  # Column name for the custom colored status

# Admin configuration for the OrderItem model
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'subtotal')  # Fields to display in the list view
    list_filter = ('order__status',)  # Filter by order status
    search_fields = ('order__order_number', 'product__name')  # Fields to search by in the admin panel
    readonly_fields = ('order', 'product', 'quantity', 'price')  # Read-only fields that cannot be edited

# Registering models for the admin panel
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Profile)

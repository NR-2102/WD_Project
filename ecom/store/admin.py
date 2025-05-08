from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Products, Profile, Order, OrderItem

# Inline configuration for displaying OrderItems within the Order admin page
class OrderItemInline(admin.TabularInline):
    model = OrderItem  # The model to display inline
    extra = 0  # No extra empty forms to show by default
    readonly_fields = ('product', 'quantity', 'price', 'subtotal')  # Fields that cannot be edited directly in the inline
    can_delete = False  # Disables the ability to delete items in the inline

    # Method to display the subtotal for each order item
    def subtotal(self, obj):
        return obj.subtotal  # Return the subtotal for the order item
    subtotal.short_description = 'Subtotal'  # Custom label for the subtotal field

# Custom admin configuration for the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Display columns in the order list view
    list_display = ('order_number', 'user', 'order_date', 'status', 'colored_status', 'total_amount')
    # Filter options in the list view
    list_filter = ('status', 'order_date')
    # Search functionality in the admin
    search_fields = ('order_number', 'user__username', 'user__email')
    # Read-only fields that cannot be edited directly in the admin form
    readonly_fields = ('order_number', 'order_date', 'total_amount')
    # Include inline OrderItems in the Order admin page
    inlines = [OrderItemInline]
    # Make 'status' field editable directly in the list view
    list_editable = ('status',)
    # Organize fields into sections in the detail view
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'order_date', 'status', 'total_amount')
        }),
        ('Shipping Information', {
            'fields': ('shipping_address', 'phone_number', 'email')
        }),
    )

    # Method to color the status field in the admin list view
    def colored_status(self, obj):
        # Define colors for different order statuses
        colors = {
            'Pending': '#FFA500',  # Orange
            'Processing': '#1E90FF',  # Blue
            'Shipped': '#4169E1',  # Royal Blue
            'Delivered': '#32CD32',  # Green
            'Cancelled': '#FF0000',  # Red
        }
        # Get the color for the current status, defaulting to gray if status not found
        color = colors.get(obj.status, '#808080')  # Default gray color
        return format_html(
            '<span style="color: white; background-color: {}; padding: 5px 10px; border-radius: 4px;">{}</span>',
            color,  # Apply the background color dynamically
            obj.status  # Display the status text
        )
    colored_status.short_description = 'Status Display'  # Custom label for the colored status field

# Admin configuration for the OrderItem model
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'subtotal')  # Columns to display in the list view
    list_filter = ('order__status',)  # Filter by the order's status
    search_fields = ('order__order_number', 'product__name')  # Search functionality for order number and product name
    readonly_fields = ('order', 'product', 'quantity', 'price')  # Read-only fields in the admin form

# Register models with Django admin
admin.site.register(Category)  # Register the Category model
admin.site.register(Products)  # Register the Products model
admin.site.register(Profile)  # Register the Profile model

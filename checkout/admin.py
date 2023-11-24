from django.contrib import admin

from .models import Order, OrderLineItem
# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
# Specify fields that should be displayed as read-only
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')
                       
# Specify the order and grouping of fields in the admin interface
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')
              
# Specify fields to be displayed in the list view of orders
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

# Specify the default ordering of orders in the admin
    ordering = ('-date',)

# Register the Order model with the OrderAdmin configuration in the Django admin
admin.site.register(Order, OrderAdmin)
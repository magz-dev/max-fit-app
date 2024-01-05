from django.contrib import admin
from .models import Order, OrderLineItem, Coupon


class OrderLineItemAdminInline(admin.TabularInline):
    # Define an inline for OrderLineItem within OrderAdmin
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # Customize the OrderAdmin interface
    inlines = (OrderLineItemAdminInline,) 
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')
    fields = ('order_number', 'user_profile', 'date', 'coupon','full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid') 

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)  # Specify the default ordering for the list view


# Register the OrderAdmin with the Order model in the admin site
admin.site.register(Order, OrderAdmin)

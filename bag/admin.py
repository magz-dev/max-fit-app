from django.contrib import admin
from .models import Coupon


# Coupon model in admin
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount']
    list_filter = ['code', 'amount']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
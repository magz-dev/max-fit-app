from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
     path('coupon_apply/', views.coupon_apply, name='coupon_apply'),
    path('coupons_manage/', views.coupons_manage, name='coupons_manage'),
    path('coupon_delete/<int:coupon_id>/\
        ', views.coupon_delete, name='coupon_delete'),
]

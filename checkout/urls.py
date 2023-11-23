from django.urls import path
from . import views

# urlpatterns for the checkout app

urlpatterns = [
    path('', views.checkout, name='checkout')
]
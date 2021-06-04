from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('orders/<int:id>', views.order_list, name='boss_orders'),
    path('time_input', views.time_input, name='time_input')
]
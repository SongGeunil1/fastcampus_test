from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('orders/<int:id>', views.order_list, name='deliver_orders'),
    path('deliver_input', views.deliver_input, name='deliver_input')
]
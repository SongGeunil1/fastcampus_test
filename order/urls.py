from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('shop_list/', views.shop_list, name='shop_list'),
    path('shop_list/<int:id>/', views.shop_detail, name='shop_detail'),
    path('menu_list/', views.menu_list, name='menu_list'),
    path('order/', views.order, name='order'),
    path('orderfood/', views.order_food, name='order_food')
    # path('admin/', admin.site.urls),
]
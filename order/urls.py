from django.urls import path
from order import views

urlpatterns = [
    path('shops/', views.shop, name="shop"),
    path('menus/<int:shop>', views.menu, name="menu"),
    path('order/',views.order, name="order")
]

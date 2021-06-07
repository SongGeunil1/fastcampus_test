from django.urls import path
from boss import views

urlpatterns = [
    path('orders/<int:shop>', views.order_list, name="order_list"),
    path('timeinput/', views.time_input, name="timeinput"),
    # path('menus/<int:shop>', views.menu, name="menu"),
    # path('order/',views.order, name="order")
]

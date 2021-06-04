from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.utils import timezone

from order.models import shops,menu,orders,order_foodlist
from order.serializers import shopsSerializer,menuSerializer,ordersSerializer,orderfoodSerializer

@csrf_exempt
def order_list(request,id):
    if request.method == 'GET':
        data = orders.objects.filter(shop=id)
        return render(request, 'boss/order_list.html', {'order_list': data})

@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        data = orders.objects.get(pk=int(request.POST['order_id']))
        data.estimated_time = request.POST['estimated_time']
        data.save()
        return render(request, 'boss/success.html')
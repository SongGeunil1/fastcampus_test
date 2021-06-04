from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render,redirect
from django.utils import timezone

from .models import shops,menu,orders,order_foodlist
from .serializers import shopsSerializer,menuSerializer,ordersSerializer,orderfoodSerializer

@csrf_exempt
def shop_list(request):
    if request.method == 'GET':
        # data = shops.objects.all()
        # serializer = shopsSerializer(data, many=True)
        # return JsonResponse(serializer.data, safe=False)
        data = shops.objects.all()
        return render(request, 'order/shop_list.html', {'shop_list': data})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = shopsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return HttpResponse(status=404)

@csrf_exempt
def shop_detail(request, id):
    try:
        shop_obj = shops.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # serializer = shopsSerializer(shop_obj)
        # return JsonResponse(serializer.data)
        menu_obj = menu.objects.filter(shop=id)
        return render(request, 'order/shop_detail.html', {'menu': menu_obj, 'id':id})


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = shopsSerializer(shop_obj, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        shop_obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def menu_list(request):
    if request.method == 'GET':
        data = menu.objects.all()
        serializer = menuSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = menuSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return HttpResponse(status=404)

@csrf_exempt
def order(request):
    if request.method == 'GET':
        data = orders.objects.all()
        # serializer = ordersSerializer(data, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'order/order_list.html', {'order_list': data})

    elif request.method == 'POST':
        food_name = request.POST.getlist('food')
        shop = request.POST['shop']
        shop_item = shops.objects.get(pk=int(shop))

        if len(food_name)==0:
            return render(request, 'order/fail.html')
        else:
            shop_item.orders_set.create(food_name=food_name[0],shop=int(shop), order_date=timezone.now())
            order_item = orders.objects.get(pk=int(shop_item.orders_set.latest('id').id))
            for food in food_name:
                order_item.order_foodlist_set.create(food_name=food)
            print(order_item.order_foodlist_set.all()[0].food_name)
            return render(request, 'order/success.html')

@csrf_exempt
def order_food(request):
    if request.method == 'GET':
        data = order_foodlist.objects.all()
        serializer = orderfoodSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

from rest_framework import serializers
from .models import shops,menu,orders,order_foodlist

class shopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shops
        fields = '__all__'
        # fields = ['id','shop_name','shop_address']

class ordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'
        # fields = ['id','shop_name','shop_address']

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ['id','shop','food_name']

class orderfoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_foodlist
        fields = '__all__'
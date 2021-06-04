from django.db import models

class shops(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=50)

class menu(models.Model):
    shop = models.ForeignKey(shops, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)

class orders(models.Model):
    food_name = models.CharField(max_length=20)
    shop = models.ForeignKey(shops, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date published')
    # address = models.CharField(max_length=20)(시발로마)
    estimated_time = models.IntegerField(default=-1)
    deliver_finish = models.BooleanField(default=0) #0: 배송중, 1: 배송완료
    cancel = models.BooleanField(default=0) #0: 취소안함, 1: 취소함

class order_foodlist(models.Model):
    order = models.ForeignKey(orders, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
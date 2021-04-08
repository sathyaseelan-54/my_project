from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# custom user models






# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,null = True,blank = True)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    digital = models.BooleanField(default = False,null = True,blank = False)
    image = models.ImageField(null = True,blank = True)

    def __str__(self):
        return self.name

    @property

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.SET_NULL,null = True,blank = True)
    date_ordred = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False,null = True,blank = True)
    transaction = models.CharField(max_length = 100,null = True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete = models.SET_NULL,null = True)
    order = models.ForeignKey(Order,on_delete = models.SET_NULL,null =  True)
    quantity = models.IntegerField(default = 0)
    date_added = models.DateTimeField(auto_now_add = True)


    @property

    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.SET_NULL,null = True)
    order = models.ForeignKey(Order,on_delete = models.SET_NULL,null = True)
    address = models.CharField(max_length = 200,null = True)
    city = models.CharField(max_length = 200,null = True)
    state = models.CharField(max_length = 200,null = True)
    pincode = models.IntegerField(null = True,blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.address



class Product_Update(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(null = True,blank = True)
    content = models.TextField(null = True,blank = True)

    def __str__(self):
        return self.title

    @property

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


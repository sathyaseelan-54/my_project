from django.contrib import admin
from .models import (
    Customer,
    Product,
    OrderItem,
    Order,
    ShippingAddress,
    Product_Update,

)



# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Product_Update)

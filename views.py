from django.shortcuts import render,redirect
from .models import *

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.views import generic

from django.views.generic import TemplateView
# Create your views here.

def index(request):
    products_update = Product_Update.objects.all()
    context = {
        'product_update': products_update
    }
    return render(request,'index.html',context)

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'product.html',context)

def mycart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,create = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()

    else:
        items = []


    context = {'items':items}
    return render(request,'mycart.html',context)

def checkout(request):
    context = {

    }
    return render(request,'checkout.html',context)



def SignUpView(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/login.html')
    else:
        form = UserCreationForm()
    return render(request,'registration/sign.html',{'form':form})
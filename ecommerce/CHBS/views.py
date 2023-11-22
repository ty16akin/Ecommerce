from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def homepage(request):
    context = {}
    return render(request, 'CHBS/homepage.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer, complete=False)
        if orders.exists():
            order = orders.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items}
    return render(request, 'CHBS/cart.html', context)

def menu(request):
    products  = Product.objects.all()
    context = {'products':products}
    return render(request, 'CHBS/menu.html', context)

def contact(request):
    context = {}
    return render(request, 'CHBS/contact.html', context)

def checkout(request):
    context = {}
    return render(request, 'CHBS/checkout.html', context)

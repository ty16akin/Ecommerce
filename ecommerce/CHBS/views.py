from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from decimal import *
import datetime
from .models import *
import json
from .utils import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.


def homepage(request):
    products  = Product.objects.all()
    context = {'products':products}
    return render(request, 'CHBS/homepage.html', context)

def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'CHBS/cart.html', context)

def menu(request):
    products  = Product.objects.all()
    context = {'products':products}
    return render(request, 'CHBS/menu.html', context)

def contact(request):
    context = {}
    return render(request, 'CHBS/contact.html', context)

def checkout(request):
       
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}

    template = render_to_string('chbs/email_template.html', context)

    email = EmailMessage(
        'Subject',
        template,
        settings.EMAIL_HOST_USER,
        ['akin0045@algonquinlive.com'],
    )

    email.fail_silently=False
    email.send()

    
    return render(request, 'CHBS/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete() 
    return JsonResponse('item was updated', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)
    
    total = round(Decimal(data['form']['total']), 2)
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            province=data['shipping']['province'],
            postalcode=data['shipping']['postal'],
        )

    print(request.body)

    return JsonResponse('Payment complete!', safe=False)
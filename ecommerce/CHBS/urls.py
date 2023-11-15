from django.urls import path
from CHBS import views

# TEMPALTE TAGGING
app_name = 'chbs'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cart/', views.cart, name='cart'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout')
]
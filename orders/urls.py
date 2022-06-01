#create_order
#create_order
from django.urls import path, include
from . import views

urlpatterns = [
     path('create_order/', views.create_order),
     path('order_master/', views.order_master),
     path('product/', views.product),
]

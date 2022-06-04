#create_order
#create_order
from django.urls import path, include
from . import views

urlpatterns = [
     path('order/', views.order),
     path('order_master/', views.order_master),
     path('products/', views.product),
     path('cursor_test/', views.cursor_test),
]

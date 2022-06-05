#create_order
#create_order
from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.order),
     path('return/<int:order_id>/', views.sales_return),
     path('update/<int:order_no>/', views.order_update),
     path('customer/<int:customer_id>/', views.customer_all_order),
     path('<int:order_no>/', views.customer_single_order),
]

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.customer),
    path('update/<int:id>/', views.customer_update),
    path('register/', views.customer_register),

]

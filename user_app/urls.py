from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.user),
    path('login/', views.login),
    path('logout/', views.logout),

]

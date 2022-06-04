from django.contrib import admin
from django.urls import path
from . import views
from . views import LoginView


urlpatterns = [
    #path('', views.user),
    path('user_account/', views.user_account),
    path('details/<str:session_key>/', views.user_info),
    path('login/', views.LoginView),
    path('logout/', views.logout),

]

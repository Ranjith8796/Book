from django.contrib import admin
from django.urls import path
from bookinfo import views

urlpatterns = [
    
    path('',views.home),
    path('addabook/', views.Add),
    path('viewb/', views.viewb),
   
]

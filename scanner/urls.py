from django.contrib import admin
from django.urls import path
from scanner import views
urlpatterns = [
    path('',views.index,name='home'),
    path('scan',views.scan,name='scan'),
]
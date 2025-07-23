from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('workers/', views.services_main_page, name="services_main_page"),
    path('details/', views.services_detail_page, name="services_detail_page"),
]

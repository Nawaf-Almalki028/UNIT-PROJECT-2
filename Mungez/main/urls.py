from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.main_page, name="home_page"),
    path('contact/', views.contact_page, name="contact_page"),
    path('services/', views.services_page, name="services_page"),
    path('about/', views.about_page, name="about_page"),
]

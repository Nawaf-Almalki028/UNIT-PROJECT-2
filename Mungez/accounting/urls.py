from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "accounting"

urlpatterns = [
    path('signup/', views.signup_page, name="signup_page"),
    path('signin/', views.signin_page, name="signin_page"),
    path('terms-of-service/', views.terms_of_service, name="terms_of_service"),
]

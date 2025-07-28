from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "accounting"

urlpatterns = [
    path('signup/', views.signup_page, name="signup_page"),
    path('signin/', views.signin_page, name="signin_page"),
    path('logout/', views.logout_page, name="logout_page"),
    path('profile/', views.profile_page, name="profile_page"),
    path('admin/', views.admin_page, name="admin_page"),
    path('admin/', views.admin_page, name="edit_user"),
    path('admin/', views.admin_page, name="activate_user"),
    path('admin/', views.admin_page, name="deactivate_user"),
    path('admin/', views.admin_page, name="delete_user"),
    path('terms-of-service/', views.terms_of_service, name="terms_of_service"),
]

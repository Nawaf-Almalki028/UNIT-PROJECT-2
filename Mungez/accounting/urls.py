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
    path('<int:user_id>/activate/', views.activate_user, name="activate_user"),
    path('<int:user_id>/deactivate/', views.deactivate_user, name="deactivate_user"),
    path('<int:user_id>/delete/', views.delete_user, name="delete_user"),
    path('terms-of-service/', views.terms_of_service, name="terms_of_service"),
]

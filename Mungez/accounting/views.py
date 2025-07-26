from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from .models import Profile

def signin_page(request:HttpRequest):
  return render(request,"main/signin_page.html")

def signup_page(request:HttpRequest):
  if request.method == "POST":
    
    xfirstname = request.POST.get("firstname")
    xlastname = request.POST.get("lastname")
    xusername = request.POST.get("username")
    xpassword = request.POST.get("password")
    xemail = request.POST.get("email")

    user = User.objects.create_user(
      username=xusername,
      password=xpassword,
      email=xemail,
      first_name=xfirstname,
      last_name=xlastname,
    )

    user.save()

    profile = Profile.objects.create(
      user=user,
      is_worker=True
    )

    profile.save()

  return render(request,"main/signup_page.html")

def terms_of_service(request:HttpRequest):
  return render(request,"main/terms_of_service.html")
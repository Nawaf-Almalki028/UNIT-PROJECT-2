from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Profile

def signin_page(request: HttpRequest):
  if request.method == "POST":
    xusername = request.POST.get("username")
    xpassword = request.POST.get("password")

    user = authenticate(request, username=xusername, password=xpassword)

    if user is not None:
      login(request, user)
      return redirect("main:home_page")
    else:
      return render(request, "main/signin_page.html", {"error":"Wrong username or password."})
    
  else:
    return render(request, "main/signin_page.html")

def signup_page(request:HttpRequest):
  if request.method == "POST":
    
    xworker = request.POST.get("auth")
    xfirstname = request.POST.get("firstname")
    xlastname = request.POST.get("lastname")
    xusername = request.POST.get("username")
    xpassword = request.POST.get("password")
    xpassword2 = request.POST.get("repeat-password")
    xemail = request.POST.get("email")

    if not all([xfirstname,xlastname,xusername,xpassword,xemail]):
      return render(request,"main/signup_page.html",{"error":"Please fill in all required fields"})
    
    if User.objects.filter(username=xusername).exists():
      return render(request,"main/signup_page.html",{"error":"This username is already taken"})
    
    if xpassword != xpassword2:
      return render(request,"main/signup_page.html",{"error":"The password and confirmation password do not match"})
       
    

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
      is_worker=xworker
    )

    profile.save()

    return redirect("accounting:signin_page")
  if request.user.is_authenticated:
    return render(request,"main/signup_page.html",{"profile":"True"})
  else:
    return render(request,"main/signup_page.html")

def terms_of_service(request:HttpRequest):
  if request.user.is_authenticated:
    return render(request,"main/terms_of_service.html",{"profile":"True"})
  else:
    return render(request,"main/terms_of_service.html")

def logout_page(request:HttpRequest):
  logout(request)
  return redirect('main:home_page')

def profile_page(request:HttpRequest):
  if request.user.is_authenticated:
    if request.method == "POST":
      profile = Profile.objects.get(user=request.user)
      profile.about=request.POST["about"]
      profile.category=request.POST["category"]
      profile.profile_img=request.FILES['image']
      profile.save()
      return redirect("accounting:profile_page")
    print(request)
    return render(request,'main/profile.html',{"profile":"True"})
  else:
    return redirect('main:home_page')

def admin_page(request:HttpRequest):
  if request.user.is_authenticated:
    # if request.method == "POST":
    #   profile = Profile.objects.get(user=request.user)
    #   profile.about=request.POST["about"]
    #   profile.category=request.POST["category"]
    #   profile.profile_img=request.FILES['image']
    #   profile.save()
    #   return redirect("accounting:profile_page")
    if request.user.is_staff:
      get_users = User.objects.all()
      return render(request,'main/admin.html',{"profile":"True","accounts":get_users})
  else:
    return redirect('main:home_page')
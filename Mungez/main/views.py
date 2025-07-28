from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def main_page(request:HttpRequest):
  if request.user.is_authenticated:
    return render(request, "main/index.html",{"profile":"True"})
  else:
    return render(request, "main/index.html")

def contact_page(request:HttpRequest):
  if request.user.is_authenticated:
    return render(request, "main/contact.html",{"profile":"True"})
  else:
    return render(request, "main/contact.html")

def services_page(request:HttpRequest):
  if request.user.is_authenticated:
    return render(request, "main/services.html",{"profile":"True"})
  else:
    return render(request, "main/services.html")

def about_page(request:HttpRequest):
  if request.user.is_authenticated:
    return render(request, "main/about.html",{"profile":"True"})
  else:
    return render(request, "main/about.html")
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def services_main_page(request:HttpRequest):
  return render(request, "main/workers.html")

def services_detail_page(request:HttpRequest):
  return render(request, "main/details.html")

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Workers,Certificates

def services_main_page(request:HttpRequest):
  get_workers = Workers.objects.all()
  return render(request, "main/workers.html",{"workers":get_workers})

def services_detail_page(request:HttpRequest, worker_id):

  get_worker = Workers.objects.get(pk= worker_id)

  return render(request, "main/details.html", {"worker":get_worker})

def add_worker(request:HttpRequest):
  worker_add = Workers(name='nawaf',about='awdwad',email='awdlwal@gmail.com',category='electrician',rating=4.2,activated=True)
  worker_add.save()
  return render(request, "main/workers.html")

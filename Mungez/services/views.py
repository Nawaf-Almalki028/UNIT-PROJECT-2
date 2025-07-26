from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Workers,Degrees,Comments

def services_main_page(request:HttpRequest):
  get_workers = Workers.objects.all()
  return render(request, "main/workers.html",{"workers":get_workers})

def services_detail_page(request: HttpRequest, worker_id):
  get_worker = Workers.objects.get(pk=worker_id)

  get_comments = Comments.objects.filter(worker_id=worker_id)

  total_raters = get_comments.count()
  rating_sum = sum(float(comment.rating) for comment in get_comments)

  average_rating = round(rating_sum / total_raters, 1) if total_raters > 0 else 0.0

  rates = {
      "raters": total_raters,
      "average": average_rating
  }

  if request.method == "POST":
    name = request.POST.get("name")
    rating = request.POST.get("rating")
    comment = request.POST.get("comment")
    if name and rating and comment:
      print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeee")
      Comments.objects.create(worker=get_worker,name=name,comment=comment,rating=rating)
      return redirect('services:services_detail_page', worker_id=worker_id)

  return render(request, "main/details.html", {"worker":get_worker,"comments":get_comments,"rate":rates})

def add_worker(request:HttpRequest):
  if request.method == "POST":
    worker_add = Workers(
      name=request.POST["name"],
      about=request.POST["about"],
      email=request.POST["email"],
      category=request.POST["category"],
      rating=request.POST["rating"],
      activated=request.POST["activated"],
      profile_img=request.FILES['image'])
    worker_add.save()
    return redirect("main:home_page")
  return render(request, "main/add.html")

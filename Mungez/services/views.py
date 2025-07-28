from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from accounting.models import Profile,Degrees,Comments,ServiceAreas
from django.contrib.auth.models import User

def services_main_page(request:HttpRequest):
  get_workers = User.objects.all()
  if request.user.is_authenticated:
    return render(request, "main/workers.html",{"workers":get_workers,"profile":"True"})
  else:
    return render(request, "main/workers.html",{"workers":get_workers})

def services_detail_page(request: HttpRequest, worker_id):
  if not request.user.is_authenticated:
      return redirect('accounting:signin_page')

  get_worker = Profile.objects.get(pk=worker_id)
  get_comments = Comments.objects.filter(profile=get_worker)

  total_raters = get_comments.count()
  rating_sum = sum(float(comment.rating) for comment in get_comments)
  average_rating = round(rating_sum / total_raters, 1) if total_raters > 0 else 0.0

  rates = {
      "raters": total_raters,
      "average": average_rating
  }

  if request.method == "POST":
      name = f"{request.user.first_name} {request.user.last_name}".strip()
      rating = request.POST.get("rating")
      comment = request.POST.get("comment")

      if name and rating and comment:
          Comments.objects.create(
              profile=get_worker,
              name=name,
              comment=comment,
              rating=float(rating)
          )
          return redirect('services:services_detail_page', worker_id=worker_id)

  return render(request, "main/details.html", {
      "worker": get_worker,
      "comments": get_comments,
      "rate": rates,
      "profile": "True"
  })

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from accounting.models import Profile,Degrees,Comments,ServiceAreas,Appointment
from django.contrib.auth.models import User
from django.db.models import Q


def services_main_page(request: HttpRequest):
  get_workers = User.objects.all()
  query = request.GET.get("q", "")
  category = request.GET.get("category", "")

  if query:
      get_workers = get_workers.filter(
          Q(username__icontains=query) |
          Q(first_name__icontains=query) |
          Q(last_name__icontains=query)
      )

  if category:
      get_workers = get_workers.filter(profile__category__iexact=category)

  if request.user.is_authenticated:
      return render(request, "main/workers.html", {"workers": get_workers, "profile": "True"})
  
  else:
      return render(request, "main/workers.html", {"workers": get_workers})

def appoiment_page(request: HttpRequest, worker:int):
  if not request.user.is_authenticated:
      return redirect('main:home_page')

  if request.method == "POST":
      date = request.POST.get("date_selected")
      times = request.POST.get("time_selected")
      comment = request.POST.get("type_issue")

      if not date or not times:
          return render(request, 'main/appoiment.html', {"profile": "True", "worker": worker, "error": "Date and time are required."})

      profile = Profile.objects.get(user=request.user)
      worker_profile = Profile.objects.get(id=worker)

      Appointment.objects.create(
          profile=profile,
          worker=worker_profile,
          date=date,
          times=times,
          comment=comment
      )
      return redirect("main:home_page")

  return render(request, 'main/appoiment.html', {"profile": "True", "worker": worker})




def services_detail_page(request: HttpRequest, worker_id):
  if not request.user.is_authenticated:
    return redirect('accounting:signin_page')

  get_worker = User.objects.get(pk=worker_id)
  get_profile = Profile.objects.get(pk=worker_id)
  get_comments = Comments.objects.filter(profile=get_profile)

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
              profile=get_profile,
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

def update_appointment(request: HttpRequest, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == "POST":
        new_date = request.POST.get("date_selected")
        new_time = request.POST.get("time_selected")
        new_comment = request.POST.get("type_issue")

        appointment.date = new_date
        appointment.times = new_time
        appointment.comment = new_comment

        appointment.save()
        return redirect("accounting:profile_page")
    return render(request, "main/apt_update.html", {"appointment": appointment})
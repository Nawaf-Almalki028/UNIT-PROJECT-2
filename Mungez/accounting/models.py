from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  CATEGORY_CHOICES = [
    ('electrician', 'Electrician'),
    ('plumber', 'Plumber'),
    ('carpenter', 'Carpenter'),
    ('mechanic', 'Mechanic'),
  ]
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_img = models.ImageField(default='images/default.jpg', upload_to='images/')
  activated = models.BooleanField(default=False)
  category = models.CharField(max_length=30,choices=CATEGORY_CHOICES)
  about = models.TextField(max_length=300)
  is_worker = models.BooleanField(default=False)

class Degrees(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="degrees")
  degree_img = models.ImageField(default='images/default.jpg', upload_to='images/')
  name = models.CharField(max_length=30)

class ServiceAreas(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="service_area")
  name = models.CharField(max_length=40)

class Comments(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
  name = models.CharField(max_length=40)
  created_at = models.DateTimeField(auto_now_add=True)
  rating = models.DecimalField(max_digits=2, decimal_places=1)
  comment = models.CharField(max_length=200)

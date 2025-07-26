from django.db import models

class Workers(models.Model):
  
  CATEGORY_CHOICES = [
    ('electrician', 'Electrician'),
    ('plumber', 'Plumber'),
    ('carpenter', 'Carpenter'),
    ('mechanic', 'Mechanic'),
  ]

  name = models.CharField(max_length=30)
  about = models.TextField(max_length=300)
  email = models.EmailField()
  category = models.CharField(max_length=30,choices=CATEGORY_CHOICES)
  rating = models.DecimalField(max_digits=2, decimal_places=1)
  created_at = models.DateTimeField(auto_now_add=True)
  profile_img = models.ImageField(default='images/default.jpg', upload_to='images/')
  activated = models.BooleanField(default=False)



class Degrees(models.Model):
  worker = models.ForeignKey(Workers, on_delete=models.CASCADE, related_name="degrees")
  name = models.CharField(max_length=30)

class ServiceAreas(models.Model):
  worker = models.ForeignKey(Workers, on_delete=models.CASCADE, related_name="service_area")
  name = models.CharField(max_length=40)

class Comments(models.Model):
  worker = models.ForeignKey(Workers, on_delete=models.CASCADE, related_name="comments")
  name = models.CharField(max_length=40)
  created_at = models.DateTimeField(auto_now_add=True)
  rating = models.DecimalField(max_digits=2, decimal_places=1)
  comment = models.CharField(max_length=200)

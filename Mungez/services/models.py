from django.db import models

class Workers(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField(max_length=1024)
    category = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=1, decimal_places=0)
    
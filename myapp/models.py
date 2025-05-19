from django.db import models

# Create your models here.

class HotelsList(models.Model):
  id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
  title = models.CharField(max_length=200)
  city = models.CharField(max_length=200, default="n/a")
  pool = models.BooleanField(default=False)
  breakfast = models.BooleanField(default=False)
  rating = models.FloatField()
  decription = models.TextField()
  price = models.IntegerField()
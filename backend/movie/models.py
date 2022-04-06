from django.db import models

# Create your models here.

# class Movie(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     genres = models.TextField()
#     watched = models.BooleanField(default=False)

#     def _str_(self):
#         return self.title

class Weather(models.Model):
    zipCode = models.TextField()
    temp = models.TextField()
from pyexpat import model
from django.db import models

# Create your models here.

class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=5)
    weather = models.CharField(max_length=120)
    date = models.DateTimeField()

    def __str__(self):
        return self.userName

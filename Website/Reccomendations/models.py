from pyexpat import model
from django.db import models

# Create your models here.

class UserData(models.Model):
    googleID = models.CharField(max_length=50)
    givenName = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=5)
    weather = models.CharField(max_length=120)
    date = models.DateTimeField()

    def __str__(self):
        return self.givenName

    
class GoogleUserData(models.Model):
    googleId = models.CharField(max_length=50, primary_key=True)
    imageUrl = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    givenName =  models.CharField(max_length=120)
    familyName =  models.CharField(max_length=120)

    def __str__(self):
        return self.givenName

class SpotifyPlaylistData(models.Model):
    external_url_spotify = models.CharField(max_length=120)
    playlist_img =  models.CharField(max_length=120)
    playlist_name = models.CharField(max_length=120)

    def __str__(self):
        return self.playlist_name

class IMDBMovieData(models.Model):
    googleId = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    image =  models.CharField(max_length=255)

    def __str__(self):
        return self.title
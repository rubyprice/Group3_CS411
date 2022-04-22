from django.contrib import admin
from .models import UserData, GoogleUserData, SpotifyPlaylistData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('googleID', 'givenName', 'zipcode', 'weather', 'date')

class GoogleUserDataAdmin(admin.ModelAdmin):
    list_display = ('googleId', 'imageUrl', 'email', 'name', 'givenName', 'familyName')

class SpotifyPlaylistDataAdmin(admin.ModelAdmin):
    list_display = ('external_url_spotify','playlist_img','playlist_name')

# Register your models here.
admin.site.register(UserData, UserDataAdmin)
admin.site.register(GoogleUserData, GoogleUserDataAdmin)
admin.site.register(SpotifyPlaylistData, SpotifyPlaylistDataAdmin)


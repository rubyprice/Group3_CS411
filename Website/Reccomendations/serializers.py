from rest_framework import serializers
from .models import UserData, GoogleUserData, SpotifyPlaylistData

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('googleID', 'givenName', 'zipcode', 'weather', 'date')



class GoogleUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUserData
        fields = ('googleId', 'imageUrl', 'email', 'name', 'givenName', 'familyName')


class SpotifyPlaylistDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyPlaylistData
        fields = ('external_url_spotify','playlist_img','playlist_name')
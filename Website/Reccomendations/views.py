import imp
from traceback import print_tb
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserDataSerializer, GoogleUserDataSerializer, SpotifyPlaylistDataSerializer
from .models import SpotifyPlaylistData, UserData, GoogleUserData

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse

import requests
import json

# Create your views here.

class UserDataView(viewsets.ModelViewSet):
    serializer_class = UserDataSerializer
    queryset = UserData.objects.all()


@csrf_exempt
def GoogleUserDataAPI(request, id=0):
     if request.method == 'POST':
        x = GoogleUserData.objects.raw('SELECT googleId FROM Reccomendations_GoogleUserData')
        print(x)
        print(dir(x))

        input()
        info = request.read().decode("utf-8")
        data = json.loads(info)
        print(data)

        google_user_serializer = GoogleUserDataSerializer(data=data)
        if google_user_serializer.is_valid():
            print('SAVING DATA')
            google_user_serializer.save()
            info = GoogleUserData.objects.all()
            google_user_serializer = GoogleUserDataSerializer(info, many=True)
            print(request.path_info)
            return HttpResponseRedirect('http://localhost:3000/DataEntry')

        return JsonResponse("Failed to Add", safe=False)


@csrf_exempt
def spotify_playlistData(request, id=0):
    if request.method == 'GET':
        print('GET spotify_playlistData')
        playlist_data = SpotifyPlaylistData.objects.all()
        playlist_serializer = SpotifyPlaylistDataSerializer(playlist_data, many=True)
        #print(playlist_serializer.data)
        return JsonResponse(playlist_serializer.data, safe=False)


@csrf_exempt
def UserDataAPI(request, id=0):
    
    if request.method == 'GET':
        print('GET')
        weather = UserData.objects.all()
        weather_serializer = UserDataSerializer(weather, many=True)
        #print(weather_serializer.data)
        return JsonResponse(weather_serializer.data, safe=False)

    elif request.method == 'POST':
        valid = False
        print('POST')
        info = str(request.read().decode("utf-8"))
        attribute_list = info.split('&')
        print(attribute_list)
        data = {}
        data['givenName'] = attribute_list[0].split('=')[1]
        googleID = attribute_list[1].split('=')[1]
        data['googleID'] = googleID
        zipcode = attribute_list[2].split('=')[1]
        data['zipcode'] = zipcode
        
        URL = "http://api.weatherapi.com/v1/current.json?q="+zipcode+"&key=22268e73aa5e421e9e4191953220604"
        response = requests.get(url = URL)
        jsonFile = response.json()
        #print(jsonFile)
        weather_condition = jsonFile['current']['condition']['text']
        print(jsonFile['current']['condition']['text'])
        data['weather'] = weather_condition
        data['date'] = jsonFile['location']['localtime']        

        print(data)
        weather_serializer = UserDataSerializer(data=data)
        if weather_serializer.is_valid():
            valid = True
            weather_serializer.save()
            weather = UserData.objects.all()
            weather_serializer = UserDataSerializer(weather, many=True)
            #print(request.path_info)
            #return HttpResponseRedirect('http://localhost:3000/DataEntry')

        

        
        URL = "https://api.spotify.com/v1/search?q=" + weather_condition.replace(' ', '%20') + "&type=playlist&offset=0&limit=5"
        payload={}
        headers = {
        'Authorization': 'Bearer BQBeaYqNASsbN-A4CE962hMW7Y9PGILa0LgMhaNdmOPni1w3oEm1KFJwsfwCE0OAY5SpAe-uN6aUIe7VRphRLoAei77sgpPEXDNXgODPLM9WgUUTKDkw-OPH4ZP0CI-6XQbOI2YUWpau_sCdJd0LjheEjAomkH8'
        }

        response = requests.request("GET", URL, headers=headers, data=payload)
        #input(response.json())
        for obj in response.json()['playlists']['items']:
            data = {}
            data['external_url_spotify'] = obj['external_urls']['spotify']
            data['playlist_img'] = obj['images'][0]['url']
            data['playlist_name'] = obj['name']

            spotify_serializer = SpotifyPlaylistDataSerializer(data=data)
            if spotify_serializer.is_valid():
                valid = True
                spotify_serializer.save()
                playlists = SpotifyPlaylistData.objects.all()
                weather_serializer = SpotifyPlaylistDataSerializer(playlists, many=True)
                #print(request.path_info)
        
        if valid:
            return HttpResponseRedirect('http://localhost:3000/DataEntry')
        else:
            return JsonResponse("Failed to Add", safe=False)
    

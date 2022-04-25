import imp
from traceback import print_tb
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserDataSerializer, GoogleUserDataSerializer, SpotifyPlaylistDataSerializer, IMDBMovieDataSerializer
from .models import SpotifyPlaylistData, UserData, GoogleUserData, IMDBMovieData

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
        return JsonResponse(playlist_serializer.data, safe=False)


@csrf_exempt
def imdb_movieData(request, id=0):
    if request.method == 'GET':
        print('GET imdb_movieData')
        movie_data = IMDBMovieData.objects.all()
        movie_datat_serializer = IMDBMovieDataSerializer(movie_data, many=True)
        return JsonResponse(movie_datat_serializer.data, safe=False)


@csrf_exempt
def UserDataAPI(request, id=0):
    
    if request.method == 'GET':
        print('GET')
        weather = UserData.objects.all()
        weather_serializer = UserDataSerializer(weather, many=True)
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
            #return HttpResponseRedirect('http://localhost:3000/DataEntry')

        

        
        URL = "https://api.spotify.com/v1/search?q=" + weather_condition.replace(' ', '%20') + "&type=playlist&offset=0&limit=5"
        payload={}
        headers = {
        'Authorization': 'Bearer BQBypxhh_JKv0F7_G9NmIYdctZYzeSeH667khbqPTxKYtLDI_lPRkuhAXmKQJSjXnJNTmP95_9dwpIHUdCC-PY7RFum9bpJDaDsr2_kMClS0PqwsKeKEdyFbI3ZQs0eat4SdnSg3jO-aN7DZrfOZsSunNKWIh8k'
        }

        response = requests.request("GET", URL, headers=headers, data=payload)
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
                spotify_serializer = SpotifyPlaylistDataSerializer(playlists, many=True)

        URL = "https://imdb-api.com/en/API/SearchMovie/k_l7zjv875/" + weather_condition.replace(' ', '%20')
        response = requests.get(URL)

        jsonPFile = response.json()
        #print(jsonPFile['results'])

        for movie in jsonPFile['results']:
            data = {}

            data['googleId'] = googleID
            data['title'] = movie['title']
            data['description'] = movie['description']
            data['image'] = movie['image']
            # print(data['googlId'])
            # print(data['title'])
            # print(data['description'])
            # print(data['image'])


            imdb_serializer = IMDBMovieDataSerializer(data=data)
            #print(data)
            #print(imdb_serializer.is_valid())
            if imdb_serializer.is_valid():
                #print('IMDBMovieDataSerializer is valid')
                valid = True
                imdb_serializer.save()
                movies = IMDBMovieData.objects.all()
                imdb_serializer = IMDBMovieDataSerializer(movies, many=True) 
        
        

        
        if valid:
            return HttpResponseRedirect('http://localhost:3000/DataEntry')
        else:
            return JsonResponse("Failed to Add", safe=False)
    

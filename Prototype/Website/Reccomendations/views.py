from traceback import print_tb
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserDataSerializer
from .models import UserData

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
def UserDataAPI(request, id=0):
    
    if request.method == 'GET':
        print('GET')
        weather = UserData.objects.all()
        weather_serializer = UserDataSerializer(weather, many=True)
        return JsonResponse(weather_serializer.data, safe=False)

    elif request.method == 'POST':
        print('POST')
        info = str(request.read().decode("utf-8"))
        attribute_list = info.split('&')
        print(attribute_list)
        data = {}
        data['userName'] = attribute_list[0].split('=')[1]
        zipcode = attribute_list[1].split('=')[1]
        data['zipcode'] = zipcode
        
        f = open('config.json')
        configdata = json.load(f)

        URL = "http://api.weatherapi.com/v1/current.json?q="+zipcode+"&key=" + configdata["weatherAPIKey"]
        response = requests.get(url = URL)
        jsonFile = response.json()
        #print(jsonFile)

        data['weather'] = jsonFile['current']['condition']['text']
        data['date'] = jsonFile['location']['localtime']


        weather_serializer = UserDataSerializer(data=data)
        if weather_serializer.is_valid():
            weather_serializer.save()
            weather = UserData.objects.all()
            weather_serializer = UserDataSerializer(weather, many=True)
            print(request.path_info)
            return HttpResponseRedirect('http://localhost:3000/')

        return JsonResponse("Failed to Add", safe=False)
    

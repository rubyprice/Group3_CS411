import requests
import json

weatherCond = 'sunny'
 
url = "https://imdb-api.com/en/API/SearchMovie/k_l7zjv875/" + weatherCond
response = requests.get(url)

jsonPFile = response.json()
#print(jsonPFile['results'])

for movie in jsonPFile['results']:
    print(movie['title'])
    print(movie['description'])
    print(movie['image'])
    print()



"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from Reccomendations import views

router = routers.DefaultRouter()
router.register(r'UserData', views.UserDataView, 'UserData')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/UserData', views.UserDataAPI),
    re_path('api/SpotifyPlaylists', views.spotify_playlistData),
    re_path('api/IMDBMovies', views.imdb_movieData),
    re_path('api/GoogleUserData', views.GoogleUserDataAPI),
    #re_path('auth/', include('djoser.social.urls')),
    #path('api/', include(router.urls))
]
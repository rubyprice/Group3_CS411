from django.urls import re_path
from Reccomendations import views


urlpatterns = [
    re_path(r'^', views.UserDataAPI)
] 

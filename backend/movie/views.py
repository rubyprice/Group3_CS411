from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie

# Create your views here.

class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
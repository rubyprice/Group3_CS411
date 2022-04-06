from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','description','genres','watched')
# Register your models here.

admin.site.register(Movie, MovieAdmin)


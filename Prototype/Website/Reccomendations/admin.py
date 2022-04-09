from django.contrib import admin
from .models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('userName', 'zipcode', 'weather', 'date')

# Register your models here.
admin.site.register(UserData, UserDataAdmin)

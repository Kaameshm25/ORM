from django.db import models
from django.contrib import admin
class footballplayer (models.Model):
    teamname=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    jersey=models.IntegerField()


class footballplayerAdmin(admin.ModelAdmin):
    list_display=('teamname','name','age','email','jersey')
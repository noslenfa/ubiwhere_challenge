from django.db import models


# Create your models here.
class Musics(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)


class Users(models.Model):
    email = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    title = models.ManyToManyField(Musics)
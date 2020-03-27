from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    album_artist = models.CharField(max_length = 100)
    album_name = models.CharField(max_length = 100)
    cover_pic = models.ImageField(upload_to = 'album_covers')
    genre = models.CharField(max_length = 50)

    def __str__(self):
        return album_name + "-by-" + album_artist

class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length = 100)
    song = models.FileField(upload_to='songs')

    def __str__(self):
        return song_title

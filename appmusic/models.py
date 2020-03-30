from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    album_name = models.CharField(max_length = 100, unique=True)
    album_artist = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    cover_pic = models.ImageField(upload_to='album_covers')

    def __str__(self):
        return self.album_name

class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    song_title = models.CharField(max_length = 100, unique=True)
    song = models.FileField(upload_to='songs')

    class Meta:
        verbose_name_plural = "Songs"

    def __str__(self):
        return self.song_title

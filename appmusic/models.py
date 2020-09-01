from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Album(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    album_name = models.CharField(max_length = 100, unique=True)
    slug = models.SlugField(max_length = 100, blank=True, null=True)
    album_artist = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    cover_pic = models.ImageField(upload_to='album_covers')

    def __str__(self):
        return self.album_name

def album_presave_reciver(sender, instance, *args, **kwargs):
    if not instance.slug or instance.slug != slugify(instance.album_name):
        instance.slug = slugify(instance.album_name)

pre_save.connect(album_presave_reciver, sender=Album)

class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    song_title = models.CharField(max_length = 100, unique=True)
    song = models.FileField(upload_to='songs')

    class Meta:
        verbose_name_plural = "Songs"

    def __str__(self):
        return self.song_title

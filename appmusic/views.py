from django.shortcuts import render, redirect, get_object_or_404
from appmusic.models import Album, Songs


def index(request):
    album_obj = Album.objects.order_by('album_name')
    return render(request, 'appmusic/index.html', {'albums': album_obj})


def about(request):
    return render(request, 'appmusic/about.html')


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'appmusic/detail.html', {'album': album})

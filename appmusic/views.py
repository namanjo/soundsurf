from django.shortcuts import render
from appmusic.models import Album, Songs

# Create your views here.
def index(request):
    album_obj = Album.objects.order_by('album_name')
    return render(request, 'appmusic/index.html', {'albums': album_obj})

def about(request):
    return render(request, 'appmusic/about.html')

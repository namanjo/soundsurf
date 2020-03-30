from django.shortcuts import render, redirect, get_object_or_404
from appmusic.models import Album, Songs
from appmusic.forms import AlbumForm, AddSongForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    album_obj = Album.objects.order_by('album_name')
    return render(request, 'appmusic/index.html', {'albums': album_obj})


def about(request):
    return render(request, 'appmusic/about.html')


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'appmusic/detail.html', {'album': album})


@login_required
def album_create(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.cover_pic = request.FILES['cover_pic']
            album.save()
            return redirect('album_detail', album_id = album.pk)
    else:
        form = AlbumForm()
    return render(request, 'appmusic/create_album.html', {'form': form})


FILE_TYPE = ['mp3', 'wav']

@login_required
def add_song(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    if request.method == "POST":
        form = AddSongForm(request.POST, request.FILES)
        if form.is_valid():
            song_obj = form.save(commit=False)
            song_obj.album = album

            song_obj.song = request.FILES['song']
            file_type = song_obj.song.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in FILE_TYPE:
                context={'form': form, "error_message": "File Format should be 'mp3' or 'wav'"}
                return render(request, 'appmusic/add_song.html', context)

            song_obj.save()
            return redirect('album_detail', album_id=album_id)
    else:
        form = AddSongForm()
    return render(request, 'appmusic/add_song.html', {'form': form})


@login_required
def album_delete(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    return redirect('index')


@login_required
def song_delete(request, song_id):
    song = Songs.objects.get(pk = song_id)
    album_id = song.album.id
    song.delete()
    return redirect('album_detail', album_id=album_id)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('index')
            else:
                return render(request, 'appmusic/login.html', {'error_message':'Account has been temporarily disabled.'})
        else:
            return render(request, 'appmusic/login.html', {'error_message': 'Invalid User Login'})
    else:
        return render(request, 'appmusic/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

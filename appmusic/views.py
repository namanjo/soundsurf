from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from appmusic.models import Album, Songs
from appmusic.forms import AlbumForm, AddSongForm, UserForm
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    is_search=False
    query = request.GET.get('q')
    if query:
        is_search = True
        albums = Album.objects.filter(
            Q(album_name__icontains=query) |
            Q(album_artist__icontains=query) |
            Q(genre__icontains=query)
        ).distinct()

        songs = Songs.objects.filter(
        Q(song_title__icontains=query)
        ).distinct()

        context = {'albums': albums, 'songs_list': songs, 'is_search': is_search}
        return render(request, 'appmusic/index.html', context)

    albums = Album.objects.all()[:12]
    songs = Songs.objects.all()[:10]
    context = {'albums': albums, 'songs_list': songs, 'is_search':is_search}
    return render(request, 'appmusic/index.html', context)


def about(request):
    return render(request, 'appmusic/about.html')


def all_albums_songs(request, its_type):
    if its_type == "songs":
        songs = Songs.objects.order_by('song_title')
        context = {'songs_list': songs, 'its_type':its_type}
        return render(request, 'appmusic/all_items.html', context)
    elif its_type == "albums":
        albums = Album.objects.order_by('album_name')
        context = {'albums': albums, 'its_type':its_type}
        return render(request, 'appmusic/all_items.html', context)
    else:
        raise Http404

@login_required
def my_albums(request):
    albums = Album.objects.filter(author=request.user)
    return render(request, 'appmusic/my_albums.html', {'albums':albums})


def detail(request, album_slug):
    album = get_object_or_404(Album, slug=album_slug)
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
            return redirect('album_detail', album_slug = album.slug)
    else:
        form = AlbumForm()
    return render(request, 'appmusic/create_album.html', {'form': form})


@login_required
def add_song(request, album_slug):
    album = get_object_or_404(Album, slug=album_slug)
    FILE_TYPE = ['mp3', 'wav']

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
            return redirect('album_detail', album_slug=album_slug)
    else:
        form = AddSongForm()
    return render(request, 'appmusic/add_song.html', {'form': form})


@login_required
def album_delete(request, album_slug):
    album = get_object_or_404(Album, album_slug=album_slug)
    album.delete()
    return redirect('index')


@login_required
def song_delete(request, song_id):
    song = get_object_or_404(Songs, pk=song_id)
    album_slug = song.album.slug
    song.delete()
    return redirect('album_detail', album_slug=album_slug)


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
            user_form = UserForm(request.POST)

            if user_form.is_valid():
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.save()

                username = user_form.cleaned_data.get('username')
                password = user_form.cleaned_data.get('password')
                user_login = authenticate(username = username, password=password)
                login(request, user_login)
                return redirect('index')

        else:
            user_form = UserForm()
        return render(request, 'appmusic/registration.html', {'form': user_form,})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
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

from appmusic.models import Album, Songs
from django import forms


class AlbumForm(forms.ModelForm):
    class Meta():
        model = Album
        exclude = ['author']


class AddSongForm(forms.ModelForm):
    class Meta():
        model = Songs
        fields = ['song_title', 'song']

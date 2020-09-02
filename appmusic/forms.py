from appmusic.models import Album, Songs
from django import forms
from django.core import validators
from django.contrib.auth.models import User


class AlbumForm(forms.ModelForm):
    class Meta():
        model = Album
        exclude = ['author', 'slug']


class AddSongForm(forms.ModelForm):
    class Meta():
        model = Songs
        fields = ['song_title', 'song']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    verify_email = forms.EmailField(label="Email again:")
    botcatcher = forms.CharField(required=False, label="",
                                widget=forms.HiddenInput(attrs={'class': 'hide_botcatcher'}),
                                validators =[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ('username', 'password','email', 'verify_email')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make Sure Emails Match")

from django.contrib.auth.models import User
from django import forms
from django.forms import HiddenInput

from music.models import Song, Album


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SongForm(forms.ModelForm):
    album = forms.ModelChoiceField(label='Album', widget=HiddenInput(), queryset=Album.objects.all())
    song_title = forms.CharField(label='Song title', max_length=100)
    file_type = forms.CharField(label='File type', max_length=10)

    class Meta:
        model = Song
        fields = ['album', 'song_title', 'file_type']

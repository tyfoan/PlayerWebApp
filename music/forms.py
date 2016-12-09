from django.contrib.auth.models import User
from django import forms

from music.models import Song


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SongForm(forms.ModelForm):
    album_id = forms.CharField(label='Album')
    song_title = forms.CharField(label='Song title', max_length=100)
    file_type = forms.CharField(label='File type', max_length=10)


    class Meta:
        model = Song
        fields = ['song_title', 'file_type', 'album_id']

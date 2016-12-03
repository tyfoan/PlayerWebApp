from django.shortcuts import render
from .models import Playlist, Video


app_name = 'video'


def index(request):
    all_playlists = Playlist.objects.all()
    return render(request, 'video/index.html',
                  context={'all_playlists': all_playlists,
                           'error_message': 'Something gone wrong'})


def detail(request, playlist_id):
    videos = Playlist.objects.get(id=playlist_id).video_set.all()
    return render(request, 'video/detail.html',
                  context={'videos': videos,
                           'error_message': 'Something gone wrong'})

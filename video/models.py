from django.db import models


class Playlist(models.Model):
    title_playlist = models.CharField(max_length=100)
    date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.title_playlist

class Video(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.video_title

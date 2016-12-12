from django.db import models
from django.core.urlresolvers import reverse


# class FileTypeManager(models.Manager):
#     def get_file_type(self):
#         return super(FileTypeManager, self).get_query_set().extra(select="song_title.split('.')[-1]")


class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.FileField()
    song_title = models.CharField(max_length=100)
    #file_type = FileTypeManager()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return '{}.{}'.format(self.song_title, self.file_type)

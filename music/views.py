from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View

from .models import Album, Song
from .forms import UserForm, SongForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


def create_song(request):
    if request.method == 'POST':
        song = SongForm(request.POST)
        if song.is_valid():
            song.save()
            return redirect(song.cleaned_data['album'].get_absolute_url())
    return redirect(song.cleaned_data['album'].get_absolute_url())


def ajax_delete_song(request, pk):
    if request.is_ajax():
        Song.objects.get(pk=pk).delete()
    return HttpResponse(request)


def ajax_like(request):
    if request.is_ajax():
        obj_type = request.POST['obj_type']
        pk = request.POST['pk']
        item_like = {'album': Album,
                     'song': Song}[obj_type].objects.get(pk=pk)
        if item_like.is_favorite:
            item_like.is_favorite = False
        else:
            item_like.is_favorite = True
        item_like.save()
    return HttpResponse(request)


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})

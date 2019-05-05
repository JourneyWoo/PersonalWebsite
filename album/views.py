from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from .forms import AlbumForm
from .models import Album
from .util import PaginatorMixin


class AlbumUpload(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    model = Album
    context_object_name = 'album'
    template_name = 'album/album_upload.html'
    fields = ['url', 'title', 'description']

    def post(self, request, *args, **kwargs):
        forms = AlbumForm(data=request.POST)
        if forms.is_valid():
            new_album = forms.save(commit=False)
            new_album.user = self.request.user
            new_album.save()
            return redirect("album:album_list")
        return self.render_to_response({"forms": forms})


class AlbumListView(PaginatorMixin, ListView):
    paginate_by = 20
    model = Album
    context_object_name = 'album'
    template_name = 'album/album_list.html'


def album_delete(request, image_id):
    if request.user.is_superuser:
        image = Album.objects.get(id=image_id)
        image.delete()
    return redirect("album:album_list")


def album_manage(request):
    album = Album.objects.all()
    return render(request, 'album/album_manage.html', {'album': album})